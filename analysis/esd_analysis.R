#!/usr/bin/env Rscript
# ESD Incident Dataset — Statistical Analysis
# Produces descriptive stats, temporal models, and trend estimates.

suppressPackageStartupMessages({
  library(dplyr)
  library(tidyr)
  library(readr)
  library(ggplot2)
  library(MASS)
  library(broom)
  library(lubridate)
})

root <- "/opt/repos/esd-research"
out  <- file.path(root, "analysis/outputs")
dir.create(out, showWarnings = FALSE, recursive = TRUE)

exp_dir <- file.path(root, "esd-dataset/exports")
pick_latest <- function(pattern) {
  f <- list.files(exp_dir, pattern = pattern, full.names = TRUE)
  stopifnot(length(f) >= 1)
  f[order(file.info(f)$mtime, decreasing = TRUE)][1]
}
inc_file <- pick_latest("large-incidents\\.csv$")
vic_file <- pick_latest("small-victims\\.csv$")
cat("Using incident file: ", inc_file, "\n", sep = "")
cat("Using victim file:   ", vic_file, "\n", sep = "")

inc <- read_csv(inc_file, show_col_types = FALSE, guess_max = 5000)
vic <- read_csv(vic_file, show_col_types = FALSE, guess_max = 5000)

# Clean colnames to snake_case-ish
names(inc) <- gsub("[^A-Za-z0-9]+", "_", names(inc)) |> tolower() |> gsub("_+$", "", x = _)
names(vic) <- gsub("[^A-Za-z0-9]+", "_", names(vic)) |> tolower() |> gsub("_+$", "", x = _)

cat_header <- function(s) cat("\n\n===== ", s, " =====\n", sep = "")

sink(file.path(out, "analysis_log.txt"), split = TRUE)

cat_header("DATASET OVERVIEW")
cat("Incident records: ", nrow(inc), "\n", sep = "")
cat("Victim records:   ", nrow(vic), "\n", sep = "")
cat("Year range (non-missing): ",
    min(inc$year, na.rm = TRUE), " to ", max(inc$year, na.rm = TRUE), "\n", sep = "")
cat("Incidents with no year:   ", sum(is.na(inc$year)), "\n", sep = "")

cat_header("VERIFICATION LEVEL BREAKDOWN")
print(inc %>% count(verification_level, sort = TRUE))

cat_header("INCIDENT TYPE BREAKDOWN")
print(inc %>% count(incident_type, sort = TRUE))

cat_header("ELECTRICAL SOURCE BREAKDOWN")
print(inc %>% count(electrical_source, sort = TRUE))

cat_header("WATER TYPE BREAKDOWN")
print(inc %>% count(water_type, sort = TRUE))

cat_header("TOP 15 STATES BY INCIDENT COUNT")
print(inc %>% count(state, sort = TRUE) %>% head(15))

cat_header("FATALITY AND INJURY TOTALS")
cat("Total fatalities: ", sum(inc$fatalities, na.rm = TRUE), "\n", sep = "")
cat("Total injuries:   ", sum(inc$injuries, na.rm = TRUE), "\n", sep = "")
cat("Total near misses:", sum(inc$near_misses, na.rm = TRUE), "\n", sep = "")

# ---- TEMPORAL DATA ----
inc_y <- inc %>% filter(!is.na(year)) %>% mutate(year = as.integer(year))

yearly <- inc_y %>%
  group_by(year) %>%
  summarise(
    incidents    = n(),
    fatalities   = sum(fatalities,  na.rm = TRUE),
    injuries     = sum(injuries,    na.rm = TRUE),
    near_misses  = sum(near_misses, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  complete(year = full_seq(year, 1),
           fill = list(incidents = 0, fatalities = 0,
                       injuries = 0, near_misses = 0))

write_csv(yearly, file.path(out, "yearly_counts.csv"))

cat_header("YEARLY COUNTS")
print(as.data.frame(yearly))

# ---- POISSON REGRESSION: incidents ~ year ----
cat_header("POISSON GLM: incidents ~ year")
m_pois <- glm(incidents ~ year, data = yearly, family = poisson())
print(summary(m_pois))
cat("\nIRR (incidence-rate ratio) per additional year: ",
    round(exp(coef(m_pois)["year"]), 4), "\n", sep = "")
ci <- confint.default(m_pois)
cat("IRR 95% CI: [",
    round(exp(ci["year", 1]), 4), ", ",
    round(exp(ci["year", 2]), 4), "]\n", sep = "")
cat("Residual deviance / df: ",
    round(m_pois$deviance / m_pois$df.residual, 3),
    " (>>1 indicates overdispersion)\n", sep = "")

# ---- NEGATIVE BINOMIAL (handles overdispersion) ----
cat_header("NEGATIVE BINOMIAL GLM: incidents ~ year")
m_nb <- tryCatch(MASS::glm.nb(incidents ~ year, data = yearly),
                 error = function(e) { cat("glm.nb failed:", conditionMessage(e), "\n"); NULL })
if (!is.null(m_nb)) {
  print(summary(m_nb))
  cat("\nIRR per year (NB): ", round(exp(coef(m_nb)["year"]), 4), "\n", sep = "")
  ci_nb <- confint.default(m_nb)
  cat("IRR 95% CI (NB): [",
      round(exp(ci_nb["year", 1]), 4), ", ",
      round(exp(ci_nb["year", 2]), 4), "]\n", sep = "")
  cat("Theta (dispersion): ", round(m_nb$theta, 3), "\n", sep = "")
}

# ---- SEGMENTED TREND: pre vs post a breakpoint ----
# ESDPA was founded ~2011. Ask whether awareness / reporting rose after.
cat_header("PRE vs POST 2011 TREND")
yearly$era <- ifelse(yearly$year >= 2011, "2011+", "pre-2011")
era_tab <- yearly %>%
  group_by(era) %>%
  summarise(years = n(),
            incidents = sum(incidents),
            mean_per_yr = mean(incidents),
            sd = sd(incidents),
            .groups = "drop")
print(era_tab)

m_era <- glm(incidents ~ era + I(year - 2011), data = yearly, family = poisson())
cat("\nPoisson model with era + centered year:\n")
print(summary(m_era))

# Interaction: does slope change after 2011?
m_int <- glm(incidents ~ era * I(year - 2011), data = yearly, family = poisson())
cat("\nInteraction model (slope change at 2011):\n")
print(summary(m_int))
cat("\nLikelihood-ratio test vs no-interaction:\n")
print(anova(m_era, m_int, test = "Chisq"))

# ---- ESTIMATE OF TRUE ANNUAL INCIDENCE via verification adjustment ----
cat_header("ADJUSTED ANNUAL INCIDENCE ESTIMATE")
# Assumption: UNVERIFIED entries have some probability of being true ESD.
# Build a sensitivity estimate using verification-level weights.
v_weights <- c(
  VERIFIED   = 1.00,
  CONFIRMED  = 0.95,
  PROBABLE   = 0.80,
  SUSPECTED  = 0.50,
  UNVERIFIED = 0.50
)
inc_w <- inc_y %>%
  mutate(w = v_weights[verification_level],
         w = ifelse(is.na(w), 0.5, w))
adj_yearly <- inc_w %>%
  group_by(year) %>%
  summarise(raw = n(),
            weighted_expected = sum(w),
            .groups = "drop")
cat("Raw annual mean: ", round(mean(adj_yearly$raw), 2), "\n", sep = "")
cat("Weighted annual mean (point estimate of true ESD events among listed): ",
    round(mean(adj_yearly$weighted_expected), 2), "\n", sep = "")
write_csv(adj_yearly, file.path(out, "yearly_verified_adjusted.csv"))

# Coverage gap: the dataset is a floor, not a census. Give a range.
# Recent decade, weighted point estimate.
recent <- adj_yearly %>% filter(year >= 2015 & year <= 2024)
cat_header("RECENT DECADE (2015–2024) SUMMARY")
cat("Mean raw listed incidents/yr:        ",
    round(mean(recent$raw), 2), "\n", sep = "")
cat("Mean weighted-listed incidents/yr:   ",
    round(mean(recent$weighted_expected), 2), "\n", sep = "")
# Undercoverage multipliers derived from phase2 net-new additions.
# 18 net-new / 175 ESDPA = ~10% underdetection just from project findings.
# Use 1.1x (low), 1.5x (central), 2.5x (high) as sensitivity band.
for (k in c(1.1, 1.5, 2.5)) {
  cat(sprintf("  Undercoverage x%.1f -> ~%.1f events/yr\n",
              k, mean(recent$weighted_expected) * k))
}

# ---- VICTIM DEMOGRAPHICS ----
cat_header("VICTIM DEMOGRAPHICS")
vic_clean <- vic %>%
  mutate(age = suppressWarnings(as.numeric(age)),
         gender = ifelse(gender %in% c("M", "F"), gender, NA))
cat("Victims with age recorded: ", sum(!is.na(vic_clean$age)), "\n", sep = "")
cat("Mean age:   ", round(mean(vic_clean$age, na.rm = TRUE), 1), "\n", sep = "")
cat("Median age: ", round(median(vic_clean$age, na.rm = TRUE), 1), "\n", sep = "")
cat("IQR: [",
    paste(round(quantile(vic_clean$age, c(.25,.75), na.rm = TRUE), 1), collapse = ", "),
    "]\n", sep = "")

cat_header("AGE BANDS")
vic_clean <- vic_clean %>%
  mutate(age_band = cut(age,
                        breaks = c(-1, 9, 14, 17, 24, 34, 49, 64, 200),
                        labels = c("0-9","10-14","15-17","18-24","25-34","35-49","50-64","65+")))
print(vic_clean %>% count(age_band))

cat_header("GENDER × OUTCOME")
print(vic_clean %>% count(gender, outcome))

# Logistic regression: probability victim is a minor given fatality?
cat_header("LOGISTIC: P(fatal outcome) ~ age + gender")
v_mod <- vic_clean %>%
  filter(!is.na(age), !is.na(gender),
         outcome %in% c("fatal","survived","injured","near_miss"))
v_mod$fatal <- as.integer(v_mod$outcome == "fatal")
m_log <- glm(fatal ~ age + gender, data = v_mod, family = binomial())
print(summary(m_log))
cat("\nOR for age (per year): ",
    round(exp(coef(m_log)["age"]), 3), "\n", sep = "")
cat("OR male vs female:       ",
    round(exp(coef(m_log)["genderM"]), 3), "\n", sep = "")

# ---- PLOTS ----
theme_set(theme_minimal(base_size = 11))

p1 <- ggplot(yearly, aes(year, incidents)) +
  geom_col(fill = "#2b7fbb") +
  geom_smooth(method = "loess", se = TRUE, color = "#c0392b", linewidth = 0.6) +
  labs(title = "ESD incidents per year (listed)",
       subtitle = sprintf("n = %d incidents with a year, %d–%d",
                          sum(yearly$incidents),
                          min(yearly$year), max(yearly$year)),
       x = NULL, y = "Incidents")
ggsave(file.path(out, "fig1_incidents_per_year.png"), p1, width = 8, height = 4.5, dpi = 150)

p2 <- yearly %>%
  dplyr::select(year, fatalities, injuries, near_misses) %>%
  pivot_longer(-year, names_to = "outcome", values_to = "n") %>%
  ggplot(aes(year, n, fill = outcome)) +
  geom_col(position = "stack") +
  scale_fill_manual(values = c(fatalities = "#c0392b",
                               injuries   = "#e67e22",
                               near_misses = "#27ae60")) +
  labs(title = "Outcomes per year", x = NULL, y = "Count", fill = NULL)
ggsave(file.path(out, "fig2_outcomes_per_year.png"), p2, width = 8, height = 4.5, dpi = 150)

if (sum(!is.na(vic_clean$age)) > 10) {
  p3 <- ggplot(vic_clean %>% filter(!is.na(age)), aes(age)) +
    geom_histogram(binwidth = 5, fill = "#2b7fbb", color = "white") +
    labs(title = "Victim age distribution",
         subtitle = sprintf("n = %d victims with recorded age",
                            sum(!is.na(vic_clean$age))),
         x = "Age", y = "Count")
  ggsave(file.path(out, "fig3_age_distribution.png"), p3, width = 7, height = 4.5, dpi = 150)
}

state_top <- inc %>% count(state, sort = TRUE) %>% filter(!is.na(state)) %>% head(15)
p4 <- ggplot(state_top, aes(reorder(state, n), n)) +
  geom_col(fill = "#2b7fbb") +
  coord_flip() +
  labs(title = "Top 15 states by listed ESD incidents",
       x = NULL, y = "Incidents")
ggsave(file.path(out, "fig4_top_states.png"), p4, width = 7, height = 5, dpi = 150)

# Verification-level share over time
ver_y <- inc_y %>%
  count(year, verification_level) %>%
  group_by(year) %>% mutate(share = n / sum(n))
p5 <- ggplot(ver_y, aes(year, n, fill = verification_level)) +
  geom_col() +
  labs(title = "Verification level composition per year",
       x = NULL, y = "Incidents", fill = "Level")
ggsave(file.path(out, "fig5_verification_over_time.png"), p5, width = 8, height = 4.5, dpi = 150)

# Fitted Poisson and NB predictions
pred_df <- data.frame(year = seq(min(yearly$year), max(yearly$year)))
pred_df$poisson_mean <- predict(m_pois, pred_df, type = "response")
if (!is.null(m_nb)) pred_df$negbin_mean <- predict(m_nb, pred_df, type = "response")

p6 <- ggplot(yearly, aes(year, incidents)) +
  geom_point(color = "grey30") +
  geom_line(data = pred_df, aes(y = poisson_mean), color = "#c0392b", linewidth = 0.8) +
  { if (!is.null(m_nb)) geom_line(data = pred_df, aes(y = negbin_mean),
                                   color = "#27ae60", linewidth = 0.8, linetype = "dashed") } +
  labs(title = "Poisson (red) and Negative-Binomial (green dashed) fits",
       x = NULL, y = "Incidents/year")
ggsave(file.path(out, "fig6_model_fits.png"), p6, width = 8, height = 4.5, dpi = 150)

cat("\n\nAll outputs written to: ", out, "\n", sep = "")
sink()
