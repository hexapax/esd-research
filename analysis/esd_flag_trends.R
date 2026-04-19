#!/usr/bin/env Rscript
# Analysis using the reasoning-classifier flags is_freshwater_private_dock
# and is_freshwater_marina. Compares them to the prior string-match setting
# (Commercial / Residential / Other-Unknown) and refits time-trend models.

suppressPackageStartupMessages({
  library(dplyr); library(tidyr); library(readr); library(ggplot2)
  library(MASS); library(stringr); library(broom); library(scales)
})

root <- "/opt/repos/esd-research"
out  <- file.path(root, "analysis/outputs")
dir.create(out, showWarnings = FALSE, recursive = TRUE)

exp_dir <- file.path(root, "esd-dataset/exports")
pick_latest <- function(pat) {
  f <- list.files(exp_dir, pattern = pat, full.names = TRUE)
  f[order(file.info(f)$mtime, decreasing = TRUE)][1]
}
inc <- read_csv(pick_latest("large-incidents\\.csv$"),
                show_col_types = FALSE, guess_max = 5000)
names(inc) <- gsub("[^A-Za-z0-9]+", "_", names(inc)) |>
  tolower() |> gsub("_+$", "", x = _)

# Normalize booleans (they arrive as strings "True"/"False")
to_bool <- function(x) tolower(as.character(x)) %in% c("true","1","yes")
inc <- inc %>%
  mutate(is_priv = to_bool(is_freshwater_private_dock),
         is_marina = to_bool(is_freshwater_marina),
         year = suppressWarnings(as.integer(year)))

# The 3-level flag setting
inc <- inc %>%
  mutate(flag_setting = case_when(
    is_priv   ~ "Private freshwater dock",
    is_marina ~ "Freshwater marina",
    TRUE      ~ "Neither"
  ))

# Rebuild the prior string-match setting to compare (copied from esd_setting_trends.R)
classify <- function(facility, bow, esrc, wtype) {
  f <- tolower(ifelse(is.na(facility), "", facility))
  b <- tolower(ifelse(is.na(bow), "", bow))
  e <- tolower(ifelse(is.na(esrc), "", esrc))
  w <- tolower(ifelse(is.na(wtype), "", wtype))
  text <- paste(f, b)
  marina_hits <- str_detect(text, paste(c(
    "marina","yacht club","yacht basin","harbor","harbour",
    "boat works","boat club","boat ramp","state park","recreation area",
    "\\bpark\\b.*(lake|river|bay|cove)","resort",
    "apartment complex","hotel","motel","condo","condominium",
    "public pool","recreational center","rec center","swim club",
    "splash pad","country club","afb","air force base","base\\b",
    "water park","campground","rv park","public dock","municipal"
  ), collapse="|"))
  resident_hits <- str_detect(text, paste(c(
    "private dock","private residence","private pool",
    "backyard","back yard","lakehouse","lake house","residence",
    "subdivision","neighborhood pool","home","family"
  ), collapse="|"))
  pool_priv <- (w=="pool") & resident_hits
  pool_com  <- (w=="pool") & (marina_hits | str_detect(text,
                "apartment|hotel|motel|condo|public|club|camp|resort|ymca|school"))
  dock_priv <- (e %in% c("dock_wiring","shore_power","boat_lift","charger")) & resident_hits
  dock_com  <- (e %in% c("dock_wiring","shore_power","boat_lift","charger")) & marina_hits
  case_when(
    pool_com  ~ "Commercial",
    pool_priv ~ "Residential",
    dock_com  ~ "Commercial",
    dock_priv ~ "Residential",
    marina_hits ~ "Commercial",
    resident_hits ~ "Residential",
    e %in% c("fountain","overhead_line","extension_cord","pool_equipment","pool_pump") &
      str_detect(text, "public|park|mall|downtown|hotel|apartment|city|municipal|school") ~ "Commercial",
    e %in% c("fountain","overhead_line","extension_cord","pool_equipment","pool_pump") &
      str_detect(text, "private|backyard|home|residence|family") ~ "Residential",
    TRUE ~ "Other/Unknown"
  )
}
inc <- inc %>% mutate(prev_setting = classify(facility_name, body_of_water,
                                               electrical_source, water_type))

sink(file.path(out, "flag_analysis_log.txt"), split = TRUE)
cat("============================================================\n")
cat(" Freshwater Private Dock / Marina — flag-based re-analysis\n")
cat("============================================================\n")

cat("\nOverall flag counts (n=", nrow(inc), "):\n", sep="")
print(inc %>% count(flag_setting))

cat("\nClassifier confidence:\n")
print(inc %>% count(setting_classifier_confidence))

# ---- Agreement with prior string-match setting ----
cat("\n=== Cross-tab: flag_setting x prev_setting (string-matched) ===\n")
ct <- inc %>% count(flag_setting, prev_setting) %>%
  pivot_wider(names_from = prev_setting, values_from = n, values_fill = 0)
print(ct)

# Agreement stats for a 2x2 collapse:
#   flag_priv  vs prev="Residential"
#   flag_mar   vs prev="Commercial"
cat("\n=== Pairwise agreement ===\n")
inc %>%
  mutate(prev_res = prev_setting == "Residential",
         prev_com = prev_setting == "Commercial") %>%
  summarise(
    priv_and_res = sum(is_priv & prev_res),
    priv_only    = sum(is_priv & !prev_res),
    res_only     = sum(!is_priv & prev_res),
    neither_pr   = sum(!is_priv & !prev_res),
    mar_and_com  = sum(is_marina & prev_com),
    mar_only     = sum(is_marina & !prev_com),
    com_only     = sum(!is_marina & prev_com),
    neither_mc   = sum(!is_marina & !prev_com)
  ) %>% print()

# Simple kappa-like concordance on the marina pairing (2x2)
k2x2 <- function(a, b) {
  t <- table(a, b)
  if (any(dim(t) < 2)) return(NA)
  po <- sum(diag(t)) / sum(t)
  pe <- sum(rowSums(t)*colSums(t)) / sum(t)^2
  (po - pe) / (1 - pe)
}
cat("\nCohen's kappa (is_priv vs prev==Residential): ",
    round(k2x2(inc$is_priv, inc$prev_setting == "Residential"), 3), "\n")
cat("Cohen's kappa (is_marina vs prev==Commercial): ",
    round(k2x2(inc$is_marina, inc$prev_setting == "Commercial"), 3), "\n")

# ---- Temporal trends per flag group ----
inc_y <- inc %>% filter(!is.na(year))
yr_rng <- seq(min(inc_y$year), max(inc_y$year))

yearly <- inc_y %>%
  count(year, flag_setting) %>%
  complete(year = yr_rng, flag_setting, fill = list(n = 0)) %>%
  rename(incidents = n)
write_csv(yearly, file.path(out, "yearly_counts_by_flag_setting.csv"))

cat("\n=== NB GLM: incidents ~ year, per flag_setting ===\n")
fit_one <- function(d) {
  m <- tryCatch(MASS::glm.nb(incidents ~ year, data = d),
                error = function(e) NULL)
  if (is.null(m)) return(tibble(
    flag_setting = d$flag_setting[1], irr = NA, ci_lo = NA, ci_hi = NA,
    p = NA, theta = NA, total = sum(d$incidents)))
  ci <- suppressMessages(confint.default(m)["year", ])
  tibble(flag_setting = d$flag_setting[1],
         irr = exp(coef(m)["year"]),
         ci_lo = exp(ci[1]), ci_hi = exp(ci[2]),
         p = summary(m)$coefficients["year","Pr(>|z|)"],
         theta = m$theta, total = sum(d$incidents))
}
tr <- bind_rows(lapply(unique(yearly$flag_setting),
                       function(s) fit_one(yearly %>% filter(flag_setting == s))))
print(tr)
write_csv(tr, file.path(out, "flag_setting_trend_models.csv"))

# ---- Segmented models ----
cat("\n=== Segmented (pre/post 2011) per flag_setting ===\n")
seg_one <- function(d) {
  d$era <- factor(ifelse(d$year >= 2011, "post","pre"), levels = c("pre","post"))
  d$yr_c <- d$year - 2011
  m1 <- tryCatch(MASS::glm.nb(incidents ~ era * yr_c, data = d),
                 error = function(e) NULL)
  if (is.null(m1)) return(tibble(flag_setting = d$flag_setting[1],
                                  pre_slope = NA, post_slope = NA, p = NA))
  co <- coef(m1)
  pre_slope <- co["yr_c"]
  post_slope <- co["yr_c"] + co["erapost:yr_c"]
  p <- summary(m1)$coefficients["erapost:yr_c","Pr(>|z|)"]
  tibble(flag_setting = d$flag_setting[1],
         pre_slope = pre_slope, post_slope = post_slope, p = p)
}
seg <- suppressWarnings(bind_rows(lapply(unique(yearly$flag_setting),
  function(s) seg_one(yearly %>% filter(flag_setting == s)))))
print(seg)
write_csv(seg, file.path(out, "flag_setting_segmented_models.csv"))

# ---- Outcome mix per flag group ----
cat("\n=== Outcome mix per flag_setting ===\n")
om <- inc %>%
  mutate(outcome = case_when(
    fatalities > 0 ~ "Fatal",
    injuries > 0   ~ "Injury only",
    near_misses > 0 ~ "Near-miss",
    TRUE ~ "Unknown")) %>%
  count(flag_setting, outcome) %>%
  group_by(flag_setting) %>%
  mutate(pct = n / sum(n)) %>% ungroup()
print(om)

# ---- PLOTS ----
theme_set(theme_minimal(base_size = 11))
pal <- c(
  "Private freshwater dock" = "#d62728",
  "Freshwater marina"       = "#1f77b4",
  "Neither"                 = "#999999"
)

# Fig A: yearly incidents by flag_setting, stacked
pA <- ggplot(yearly,
             aes(year, incidents, fill = flag_setting)) +
  geom_col() +
  scale_fill_manual(values = pal) +
  labs(title = "ESD incidents per year by reasoning-classifier setting",
       subtitle = "Private-dock / Marina flags (fresh water only); 'Neither' includes pools, salt water, flooded structures, and ambiguous cases",
       x = NULL, y = "Incidents", fill = NULL) +
  theme(legend.position = "top")
ggsave(file.path(out, "fig12_flag_yearly_stacked.png"), pA,
       width = 9, height = 5, dpi = 150)

# Fig B: LOESS per group
pB <- ggplot(yearly, aes(year, incidents,
                         color = flag_setting, fill = flag_setting)) +
  geom_col(alpha = 0.35, color = NA, position = "dodge") +
  geom_smooth(method = "loess", se = TRUE, span = 0.6, linewidth = 0.9) +
  scale_color_manual(values = pal) + scale_fill_manual(values = pal) +
  labs(title = "Flag-classified settings — yearly counts with LOESS smoother",
       x = NULL, y = "Incidents", color = NULL, fill = NULL) +
  theme(legend.position = "top")
ggsave(file.path(out, "fig13_flag_yearly_loess.png"), pB,
       width = 9, height = 5, dpi = 150)

# Fig C: NB fits faceted
pred_df <- yearly %>%
  group_by(flag_setting) %>%
  group_modify(~{
    m <- tryCatch(MASS::glm.nb(incidents ~ year, data = .x), error = function(e) NULL)
    if (is.null(m)) return(tibble(year = .x$year, fit = NA_real_))
    tibble(year = .x$year, fit = predict(m, newdata = .x, type = "response"))
  }) %>% ungroup()

pC <- ggplot(yearly, aes(year, incidents)) +
  geom_col(aes(fill = flag_setting), alpha = 0.85) +
  geom_line(data = pred_df, aes(y = fit), color = "black", linewidth = 0.6) +
  facet_wrap(~flag_setting, ncol = 1, scales = "free_y") +
  scale_fill_manual(values = pal, guide = "none") +
  labs(title = "Flag-classified settings — per-group NB trend fits",
       x = NULL, y = "Incidents")
ggsave(file.path(out, "fig14_flag_faceted_nb.png"), pC,
       width = 9, height = 7, dpi = 150)

# Fig D: rolling share
suppressPackageStartupMessages(library(zoo))
roll_share <- yearly %>%
  arrange(year) %>%
  group_by(flag_setting) %>%
  mutate(roll5 = zoo::rollmean(incidents, k = 5, fill = NA, align = "center")) %>%
  ungroup() %>%
  group_by(year) %>%
  mutate(share = roll5 / sum(roll5, na.rm = TRUE)) %>%
  ungroup()

pD <- ggplot(roll_share %>% filter(!is.na(share)),
             aes(year, share, fill = flag_setting)) +
  geom_area(alpha = 0.9) +
  scale_fill_manual(values = pal) +
  scale_y_continuous(labels = scales::percent_format(accuracy = 1)) +
  labs(title = "Share of listed incidents by flag-classified setting (5-yr rolling)",
       x = NULL, y = "Share", fill = NULL) +
  theme(legend.position = "top")
ggsave(file.path(out, "fig15_flag_share_over_time.png"), pD,
       width = 9, height = 5, dpi = 150)

# Fig E: agreement confusion (flag setting vs string-matched setting)
ct_long <- inc %>% count(flag_setting, prev_setting)
pE <- ggplot(ct_long, aes(prev_setting, flag_setting, fill = n)) +
  geom_tile(color = "white") +
  geom_text(aes(label = n), color = "black", size = 4) +
  scale_fill_gradient(low = "#ecf6fc", high = "#1f77b4") +
  labs(title = "Reasoning-classifier flags vs prior string-matched setting",
       subtitle = "Counts of incidents in each cell (n = 201)",
       x = "Prior string-matched setting", y = "Flag-classified setting") +
  theme(legend.position = "right")
ggsave(file.path(out, "fig16_flag_vs_prior_setting.png"), pE,
       width = 8, height = 4.5, dpi = 150)

# Fig F: outcome mix per flag group
pF <- ggplot(om, aes(flag_setting, n, fill = outcome)) +
  geom_col(position = "fill") +
  scale_y_continuous(labels = scales::percent_format(accuracy = 1)) +
  scale_fill_manual(values = c(Fatal="#c0392b", `Injury only`="#e67e22",
                               `Near-miss`="#27ae60", Unknown="#999999")) +
  labs(title = "Outcome composition per flag-classified setting",
       x = NULL, y = "Share", fill = NULL)
ggsave(file.path(out, "fig17_flag_outcome_mix.png"), pF,
       width = 8, height = 4.5, dpi = 150)

# ---- Fatality risk logistic: fatal ~ flag group ----
cat("\n=== Logistic: P(fatality) ~ flag_setting ===\n")
inc$any_fatal <- inc$fatalities > 0
m_log <- glm(any_fatal ~ flag_setting, data = inc, family = binomial())
print(summary(m_log))
cat("\nOdds ratios:\n")
print(round(exp(cbind(coef(m_log), confint.default(m_log))), 3))

cat("\nAll flag-analysis outputs written to: ", out, "\n", sep = "")
sink()
