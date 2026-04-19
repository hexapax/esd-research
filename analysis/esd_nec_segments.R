#!/usr/bin/env Rscript
# NEC-era segmented trend analysis for flag-classified settings.
# Tests whether marina incidents (subject to NEC 555) bend down after 2011/2017
# while private-dock incidents (not subject to 555) do not.

suppressPackageStartupMessages({
  library(dplyr); library(tidyr); library(readr); library(ggplot2)
  library(MASS); library(broom); library(scales); library(zoo)
})

root <- "/opt/repos/esd-research"
out  <- file.path(root, "analysis/outputs")
exp_dir <- file.path(root, "esd-dataset/exports")
pick_latest <- function(pat) {
  f <- list.files(exp_dir, pattern = pat, full.names = TRUE)
  f[order(file.info(f)$mtime, decreasing = TRUE)][1]
}
inc <- read_csv(pick_latest("large-incidents\\.csv$"),
                show_col_types = FALSE, guess_max = 5000)
names(inc) <- gsub("[^A-Za-z0-9]+", "_", names(inc)) |>
  tolower() |> gsub("_+$", "", x = _)

to_bool <- function(x) tolower(as.character(x)) %in% c("true","1","yes")
inc <- inc %>%
  mutate(is_priv   = to_bool(is_freshwater_private_dock),
         is_marina = to_bool(is_freshwater_marina),
         year      = suppressWarnings(as.integer(year)),
         flag_setting = case_when(
           is_priv   ~ "Private freshwater dock",
           is_marina ~ "Freshwater marina",
           TRUE      ~ "Neither"
         )) %>%
  filter(!is.na(year))

yr_rng <- seq(min(inc$year), max(inc$year))

yearly <- inc %>%
  count(year, flag_setting) %>%
  complete(year = yr_rng, flag_setting, fill = list(n = 0)) %>%
  rename(incidents = n)

# Restrict setting-specific models to the two flag-true groups
dock_groups <- c("Private freshwater dock", "Freshwater marina")
yearly_dm <- yearly %>% filter(flag_setting %in% dock_groups)

sink(file.path(out, "nec_segment_log.txt"), split = TRUE)
cat("============================================================\n")
cat(" NEC-era segmented trend analysis\n")
cat(" Settings: Private freshwater dock (not covered by NEC 555)\n")
cat("           Freshwater marina (covered by NEC 555)\n")
cat("============================================================\n")
cat("Sample sizes by year range and flag_setting:\n\n")

# ---- 2-SEGMENT: break at 2011 ----
cat("\n========== TWO-SEGMENT MODEL (break at 2011) ==========\n")
yearly_dm <- yearly_dm %>%
  mutate(era2 = factor(ifelse(year >= 2011, "B: 2011+", "A: pre-2011"),
                       levels = c("A: pre-2011", "B: 2011+")),
         yrc  = year - 2011,
         flag = factor(flag_setting, levels = dock_groups))

cat("\nN per era x setting:\n")
print(yearly_dm %>%
        mutate(has = ifelse(incidents > 0, 1, 0)) %>%
        group_by(era2, flag_setting) %>%
        summarise(years = n(), total_incidents = sum(incidents),
                  per_yr = mean(incidents), .groups = "drop"))

m2_null <- MASS::glm.nb(incidents ~ flag + yrc, data = yearly_dm)
m2_era  <- MASS::glm.nb(incidents ~ flag + era2 + yrc, data = yearly_dm)
m2_int  <- MASS::glm.nb(incidents ~ flag * (era2 + yrc), data = yearly_dm)
m2_slope<- MASS::glm.nb(incidents ~ flag * era2 * yrc,   data = yearly_dm)

cat("\nModel comparison (AIC):\n")
cat(sprintf("  base flag+yr           AIC=%.1f\n", AIC(m2_null)))
cat(sprintf("  + era step             AIC=%.1f\n", AIC(m2_era)))
cat(sprintf("  + flag*(era+yr)        AIC=%.1f\n", AIC(m2_int)))
cat(sprintf("  + flag*era*yr (full)   AIC=%.1f\n", AIC(m2_slope)))

cat("\nLR tests:\n")
print(anova(m2_null, m2_era,  test = "Chisq"))
print(anova(m2_era,  m2_int,  test = "Chisq"))
print(anova(m2_int,  m2_slope, test = "Chisq"))

cat("\nPer-group slopes (IRR/yr) by era from the full interaction model:\n")
pred_slopes_2 <- expand.grid(
  flag = factor(dock_groups, levels = dock_groups),
  era2 = factor(c("A: pre-2011","B: 2011+"),
                levels = c("A: pre-2011","B: 2011+")),
  yrc  = c(0, 1)  # derive slope as log(f(1)) - log(f(0))
)
pred_slopes_2$mu <- predict(m2_slope, pred_slopes_2, type = "response")
slopes2 <- pred_slopes_2 %>%
  group_by(flag, era2) %>%
  summarise(slope_log = log(mu[yrc==1]) - log(mu[yrc==0]),
            irr = exp(slope_log), .groups = "drop")
print(slopes2)

# ---- 3-SEGMENT: break at 2011 and 2017 ----
cat("\n\n========== THREE-SEGMENT MODEL (breaks at 2011 and 2017) ==========\n")
yearly_dm <- yearly_dm %>%
  mutate(era3 = cut(year, breaks = c(-Inf, 2010, 2016, Inf),
                    labels = c("A: pre-2011","B: 2011-2016","C: 2017+")),
         yrc2 = year - 2017)  # centered for stability, arbitrary

cat("\nN per era x setting:\n")
print(yearly_dm %>%
        group_by(era3, flag_setting) %>%
        summarise(years = n(), total_incidents = sum(incidents),
                  per_yr = round(mean(incidents), 2), .groups = "drop"))

m3_null <- MASS::glm.nb(incidents ~ flag + yrc2, data = yearly_dm)
m3_era  <- MASS::glm.nb(incidents ~ flag + era3 + yrc2, data = yearly_dm)
m3_int  <- MASS::glm.nb(incidents ~ flag * (era3 + yrc2), data = yearly_dm)
m3_slope<- MASS::glm.nb(incidents ~ flag * era3 * yrc2, data = yearly_dm)

cat("\nModel comparison (AIC):\n")
cat(sprintf("  base flag+yr           AIC=%.1f\n", AIC(m3_null)))
cat(sprintf("  + era step (3 levels)  AIC=%.1f\n", AIC(m3_era)))
cat(sprintf("  + flag*(era+yr)        AIC=%.1f\n", AIC(m3_int)))
cat(sprintf("  + flag*era*yr (full)   AIC=%.1f\n", AIC(m3_slope)))

cat("\nLR tests:\n")
print(anova(m3_null, m3_era,  test = "Chisq"))
print(anova(m3_era,  m3_int,  test = "Chisq"))
print(anova(m3_int,  m3_slope, test = "Chisq"))

# Per-group per-era slopes from the 3-segment full model
cat("\nPer-group per-era IRR (from full interaction model):\n")
pred3 <- expand.grid(
  flag = factor(dock_groups, levels = dock_groups),
  era3 = factor(levels(yearly_dm$era3), levels = levels(yearly_dm$era3)),
  yrc2 = c(0, 1)
)
pred3$mu <- predict(m3_slope, pred3, type = "response")
slopes3 <- pred3 %>%
  group_by(flag, era3) %>%
  summarise(slope_log = log(mu[yrc2 == 1]) - log(mu[yrc2 == 0]),
            irr = exp(slope_log), .groups = "drop")
print(slopes3)

# ---- Simple per-era mean rate (robust sanity check) ----
cat("\nMean incidents/yr per era x setting (raw):\n")
era_means <- yearly_dm %>%
  group_by(era3, flag_setting) %>%
  summarise(years = n(),
            total = sum(incidents),
            mean_per_yr = mean(incidents),
            sd         = sd(incidents), .groups = "drop")
print(era_means)
write_csv(era_means, file.path(out, "nec_era_means.csv"))

# Ratio of marina vs private-dock per era
cat("\nMarina / Private-dock incident-rate ratio per era:\n")
era_ratio <- era_means %>%
  dplyr::select(era3, flag_setting, mean_per_yr) %>%
  pivot_wider(names_from = flag_setting, values_from = mean_per_yr) %>%
  mutate(ratio_marina_over_priv = `Freshwater marina` /
           pmax(`Private freshwater dock`, 1e-9))
print(era_ratio)

# ---- PLOTS ----
theme_set(theme_minimal(base_size = 11))
pal <- c("Private freshwater dock" = "#d62728",
         "Freshwater marina"       = "#1f77b4")

# Fig 18: 2-segment visual
break_years_2 <- c(2011)
yearly_dm_f <- yearly_dm %>% filter(flag_setting %in% dock_groups)
pred_fit2 <- yearly_dm_f
pred_fit2$fit <- predict(m2_slope, pred_fit2, type = "response")

p18 <- ggplot(yearly_dm_f, aes(year, incidents, color = flag_setting)) +
  geom_col(aes(fill = flag_setting), alpha = 0.7, color = NA,
           position = position_dodge(width = 0.7), width = 0.7) +
  geom_line(data = pred_fit2, aes(y = fit, group = flag_setting),
            linewidth = 0.9) +
  geom_vline(xintercept = break_years_2 - 0.5,
             linetype = "dashed", color = "black", alpha = 0.5) +
  annotate("text", x = break_years_2, y = Inf, vjust = 1.5, hjust = -0.1,
           label = "NEC 2011", size = 3, color = "black") +
  scale_color_manual(values = pal) + scale_fill_manual(values = pal) +
  labs(title = "Two-segment NB fit: slopes change at NEC 2011",
       subtitle = "Fresh-water private dock vs. fresh-water marina only",
       x = NULL, y = "Incidents", color = NULL, fill = NULL) +
  theme(legend.position = "top")
ggsave(file.path(out, "fig18_nec_2seg.png"), p18,
       width = 9, height = 5, dpi = 150)

# Fig 19: 3-segment visual
break_years_3 <- c(2011, 2017)
pred_fit3 <- yearly_dm_f
pred_fit3$fit <- predict(m3_slope, pred_fit3, type = "response")

p19 <- ggplot(yearly_dm_f, aes(year, incidents, color = flag_setting)) +
  geom_col(aes(fill = flag_setting), alpha = 0.7, color = NA,
           position = position_dodge(width = 0.7), width = 0.7) +
  geom_line(data = pred_fit3, aes(y = fit, group = flag_setting),
            linewidth = 0.9) +
  geom_vline(xintercept = break_years_3 - 0.5,
             linetype = "dashed", color = "black", alpha = 0.5) +
  annotate("text", x = 2011, y = Inf, vjust = 1.5, hjust = -0.1,
           label = "NEC 2011", size = 3, color = "black") +
  annotate("text", x = 2017, y = Inf, vjust = 1.5, hjust = -0.1,
           label = "NEC 2017", size = 3, color = "black") +
  scale_color_manual(values = pal) + scale_fill_manual(values = pal) +
  labs(title = "Three-segment NB fit: slopes change at NEC 2011 and NEC 2017",
       subtitle = "Fresh-water private dock vs. fresh-water marina only",
       x = NULL, y = "Incidents", color = NULL, fill = NULL) +
  theme(legend.position = "top")
ggsave(file.path(out, "fig19_nec_3seg.png"), p19,
       width = 9, height = 5, dpi = 150)

# Fig 20: per-era mean incidence bar chart
p20 <- ggplot(era_means, aes(era3, mean_per_yr, fill = flag_setting)) +
  geom_col(position = "dodge") +
  geom_text(aes(label = sprintf("%.1f\n(n=%d)", mean_per_yr, total)),
            position = position_dodge(width = 0.9),
            vjust = -0.2, size = 3) +
  scale_fill_manual(values = pal) +
  labs(title = "Mean incidents per year, by NEC era and flag setting",
       subtitle = "Era A = pre-2011, B = 2011–2016 (NEC 2011/2014), C = 2017+ (NEC 2017 and later)",
       x = NULL, y = "Mean incidents / year", fill = NULL) +
  theme(legend.position = "top") +
  coord_cartesian(ylim = c(0, max(era_means$mean_per_yr) * 1.25))
ggsave(file.path(out, "fig20_nec_era_means.png"), p20,
       width = 9, height = 5, dpi = 150)

# Fig 21: piecewise-linear ribbons
# Build tidy per-era piecewise fits manually for presentation
piecewise_df <- yearly_dm %>%
  dplyr::select(year, flag_setting, era3, incidents)
fits_per_era <- piecewise_df %>%
  group_by(flag_setting, era3) %>%
  group_modify(~{
    d <- .x
    if (sum(d$incidents) == 0 || nrow(d) < 3) {
      return(tibble(year = d$year, fit = NA_real_))
    }
    m <- tryCatch(MASS::glm.nb(incidents ~ year, data = d),
                  error = function(e) NULL)
    if (is.null(m)) return(tibble(year = d$year, fit = NA_real_))
    tibble(year = d$year, fit = predict(m, newdata = d, type = "response"))
  }) %>% ungroup()

p21 <- ggplot(piecewise_df, aes(year, incidents, color = flag_setting)) +
  geom_point(alpha = 0.6) +
  geom_line(data = fits_per_era, aes(y = fit, color = flag_setting,
                                      group = interaction(flag_setting, era3)),
            linewidth = 1) +
  geom_vline(xintercept = break_years_3 - 0.5,
             linetype = "dashed", color = "black", alpha = 0.5) +
  annotate("text", x = 2011, y = Inf, vjust = 1.5, hjust = -0.1,
           label = "NEC 2011", size = 3) +
  annotate("text", x = 2017, y = Inf, vjust = 1.5, hjust = -0.1,
           label = "NEC 2017", size = 3) +
  scale_color_manual(values = pal) +
  facet_wrap(~flag_setting, ncol = 1) +
  labs(title = "Per-era independent NB fits",
       subtitle = "Each era fit separately; slope is the trend within that era",
       x = NULL, y = "Incidents", color = NULL) +
  theme(legend.position = "none")
ggsave(file.path(out, "fig21_nec_piecewise.png"), p21,
       width = 9, height = 6, dpi = 150)

# IRR table (per era, per setting) with CIs — fit simple per-era NB
per_era_irr <- piecewise_df %>%
  group_by(flag_setting, era3) %>%
  group_modify(~{
    d <- .x
    if (sum(d$incidents) < 3 || nrow(d) < 3 ||
        length(unique(d$year)) < 2) {
      return(tibble(irr = NA, ci_lo = NA, ci_hi = NA, p = NA,
                    total = sum(d$incidents), years = nrow(d)))
    }
    m <- tryCatch(MASS::glm.nb(incidents ~ year, data = d),
                  error = function(e) NULL)
    if (is.null(m)) {
      return(tibble(irr = NA, ci_lo = NA, ci_hi = NA, p = NA,
                    total = sum(d$incidents), years = nrow(d)))
    }
    ci <- suppressMessages(confint.default(m)["year", ])
    tibble(irr = exp(coef(m)["year"]),
           ci_lo = exp(ci[1]),
           ci_hi = exp(ci[2]),
           p = summary(m)$coefficients["year","Pr(>|z|)"],
           total = sum(d$incidents), years = nrow(d))
  }) %>% ungroup()
cat("\nPer-era per-setting IRR/yr (simple NB within each era):\n")
print(per_era_irr)
write_csv(per_era_irr, file.path(out, "nec_era_per_setting_irr.csv"))

cat("\nAll NEC-era outputs written to: ", out, "\n", sep = "")
sink()
