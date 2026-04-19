#!/usr/bin/env Rscript
# Marina vs Residential setting trends.
# Classifies each incident into Marina / Residential / Other from facility_name,
# body_of_water, and electrical_source, then fits trend models per setting.

suppressPackageStartupMessages({
  library(dplyr); library(tidyr); library(readr); library(ggplot2)
  library(MASS); library(stringr); library(broom)
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

# ---- Classification ----
# Marina / Commercial: marina/harbor/yacht/resort/boat works/AFB marina,
#   hotel/apartment/commercial pools, state-park facilities, splash pads.
# Residential: private dock, private pool, backyard, lakehouse, subdivision,
#   "private residence", family-named facilities.
# Other: unlabeled or non-dock/non-pool (fountains, flooded streets, cornfield, etc.)

classify <- function(facility, bow, esrc, wtype) {
  f <- tolower(ifelse(is.na(facility), "", facility))
  b <- tolower(ifelse(is.na(bow), "", bow))
  e <- tolower(ifelse(is.na(esrc), "", esrc))
  w <- tolower(ifelse(is.na(wtype), "", wtype))
  text <- paste(f, b)

  marina_hits <- str_detect(text, paste(c(
    "marina", "yacht club", "yacht basin", "harbor", "harbour",
    "boat works", "boat club", "boat ramp", "state park", "recreation area",
    "\\bpark\\b.*(lake|river|bay|cove)", "resort",
    "apartment complex", "hotel", "motel", "condo", "condominium",
    "public pool", "recreational center", "rec center", "swim club",
    "splash pad", "country club", "afb", "air force base", "base\\b",
    "water park", "campground", "rv park", "public dock", "municipal"
  ), collapse = "|"))

  resident_hits <- str_detect(text, paste(c(
    "private dock", "private residence", "private pool",
    "backyard", "back yard", "lakehouse", "lake house", "residence",
    "subdivision", "neighborhood pool", "home", "family"
  ), collapse = "|"))

  # electrical source refinements
  pool_priv <- (w == "pool") & resident_hits
  pool_com  <- (w == "pool") & (marina_hits | str_detect(text,
                "apartment|hotel|motel|condo|public|club|camp|resort|ymca|school"))
  dock_priv <- (e %in% c("dock_wiring","shore_power","boat_lift","charger")) & resident_hits
  dock_com  <- (e %in% c("dock_wiring","shore_power","boat_lift","charger")) & marina_hits

  case_when(
    pool_com                          ~ "Commercial",
    pool_priv                         ~ "Residential",
    dock_com                          ~ "Commercial",
    dock_priv                         ~ "Residential",
    marina_hits                       ~ "Commercial",
    resident_hits                     ~ "Residential",
    e %in% c("fountain","overhead_line","extension_cord","pool_equipment","pool_pump") &
      str_detect(text, "public|park|mall|downtown|hotel|apartment|city|municipal|school") ~ "Commercial",
    e %in% c("fountain","overhead_line","extension_cord","pool_equipment","pool_pump") &
      str_detect(text, "private|backyard|home|residence|family") ~ "Residential",
    TRUE ~ "Other/Unknown"
  )
}

inc <- inc %>%
  mutate(setting = classify(facility_name, body_of_water,
                            electrical_source, water_type),
         year = suppressWarnings(as.integer(year)))

# Save classified table for auditing
write_csv(
  inc %>% dplyr::select(incident_id, year, state, facility_name, body_of_water,
                        electrical_source, water_type, setting),
  file.path(out, "incidents_with_setting.csv")
)

cat("=== Setting counts ===\n")
print(inc %>% count(setting, sort = TRUE))
cat("\n=== Setting x electrical_source ===\n")
print(inc %>% count(setting, electrical_source) %>%
        tidyr::pivot_wider(names_from = setting, values_from = n, values_fill = 0))

# ---- Yearly counts per setting ----
inc_y <- inc %>% filter(!is.na(year))
yr_rng <- seq(min(inc_y$year), max(inc_y$year))

yearly_set <- inc_y %>%
  count(year, setting) %>%
  complete(year = yr_rng, setting, fill = list(n = 0)) %>%
  rename(incidents = n)

write_csv(yearly_set, file.path(out, "yearly_counts_by_setting.csv"))

# ---- Model per setting: NB GLM with year term ----
cat("\n=== NB GLM: incidents ~ year, per setting ===\n")
fit_one <- function(d) {
  tryCatch({
    m <- MASS::glm.nb(incidents ~ year, data = d)
    ci <- suppressMessages(confint.default(m)["year", ])
    tibble(
      setting = d$setting[1],
      irr = exp(coef(m)["year"]),
      ci_lo = exp(ci[1]),
      ci_hi = exp(ci[2]),
      p = summary(m)$coefficients["year","Pr(>|z|)"],
      theta = m$theta,
      n_years_nonzero = sum(d$incidents > 0),
      total = sum(d$incidents)
    )
  }, error = function(e) {
    tibble(setting = d$setting[1],
           irr = NA, ci_lo = NA, ci_hi = NA, p = NA, theta = NA,
           n_years_nonzero = sum(d$incidents > 0), total = sum(d$incidents))
  })
}
settings <- unique(yearly_set$setting)
res <- bind_rows(lapply(settings, function(s)
  fit_one(yearly_set %>% filter(setting == s))))
print(res)
write_csv(res, file.path(out, "setting_trend_models.csv"))

# ---- Segmented (pre/post 2011) per setting ----
cat("\n=== Segmented model (slope change at 2011), per setting ===\n")
seg_one <- function(d) {
  d$era <- factor(ifelse(d$year >= 2011, "post","pre"), levels = c("pre","post"))
  d$yr_c <- d$year - 2011
  m0 <- tryCatch(MASS::glm.nb(incidents ~ era + yr_c, data = d), error = function(e) NULL)
  m1 <- tryCatch(MASS::glm.nb(incidents ~ era * yr_c, data = d), error = function(e) NULL)
  if (is.null(m0) || is.null(m1)) {
    return(tibble(setting = d$setting[1], pre_slope = NA, post_slope = NA,
                  slope_change_p = NA))
  }
  co <- coef(m1)
  pre_slope  <- co["yr_c"]
  post_slope <- co["yr_c"] + co["erapost:yr_c"]
  pval <- summary(m1)$coefficients["erapost:yr_c","Pr(>|z|)"]
  tibble(setting = d$setting[1],
         pre_slope = pre_slope, post_slope = post_slope,
         slope_change_p = pval)
}
seg <- bind_rows(lapply(settings, function(s)
  seg_one(yearly_set %>% filter(setting == s))))
print(seg)
write_csv(seg, file.path(out, "setting_segmented_models.csv"))

# ---- Plots ----
theme_set(theme_minimal(base_size = 11))
pal <- c(Commercial = "#1f77b4",
         Residential = "#d62728",
         `Other/Unknown` = "#7f7f7f")

# Plot A: side-by-side yearly counts with LOESS
pA <- ggplot(yearly_set, aes(year, incidents, color = setting, fill = setting)) +
  geom_col(position = "dodge", alpha = 0.35, color = NA) +
  geom_smooth(method = "loess", se = TRUE, span = 0.6, linewidth = 0.9) +
  scale_color_manual(values = pal) + scale_fill_manual(values = pal) +
  labs(title = "ESD incidents per year by setting",
       subtitle = "Bars = raw counts; curves = LOESS smoother (span 0.6)",
       x = NULL, y = "Incidents", color = NULL, fill = NULL) +
  theme(legend.position = "top")
ggsave(file.path(out, "fig7_setting_yearly_loess.png"), pA,
       width = 9, height = 5, dpi = 150)

# Plot B: faceted bars with NB fit overlay
pred_df <- yearly_set %>%
  group_by(setting) %>%
  group_modify(~{
    m <- tryCatch(MASS::glm.nb(incidents ~ year, data = .x), error = function(e) NULL)
    if (is.null(m)) return(tibble(year = .x$year, fit = NA_real_))
    tibble(year = .x$year, fit = predict(m, newdata = .x, type = "response"))
  }) %>% ungroup()

pB <- ggplot(yearly_set, aes(year, incidents)) +
  geom_col(aes(fill = setting), alpha = 0.85) +
  geom_line(data = pred_df, aes(y = fit), color = "black", linewidth = 0.6) +
  facet_wrap(~setting, ncol = 1, scales = "free_y") +
  scale_fill_manual(values = pal, guide = "none") +
  labs(title = "ESD incidents per year by setting (NB fit overlaid)",
       x = NULL, y = "Incidents")
ggsave(file.path(out, "fig8_setting_faceted_nb.png"), pB,
       width = 9, height = 7, dpi = 150)

# Plot C: proportions over time (5-yr rolling share)
roll_share <- yearly_set %>%
  arrange(year) %>%
  group_by(setting) %>%
  mutate(roll5 = zoo::rollmean(incidents, k = 5, fill = NA, align = "center")) %>%
  ungroup() %>%
  group_by(year) %>%
  mutate(share = roll5 / sum(roll5, na.rm = TRUE)) %>%
  ungroup()

pC <- ggplot(roll_share %>% filter(!is.na(share)),
             aes(year, share, fill = setting)) +
  geom_area(alpha = 0.85) +
  scale_fill_manual(values = pal) +
  scale_y_continuous(labels = scales::percent_format(accuracy = 1)) +
  labs(title = "Setting composition over time (5-year rolling share)",
       x = NULL, y = "Share of incidents", fill = NULL) +
  theme(legend.position = "top")
ggsave(file.path(out, "fig9_setting_share_over_time.png"), pC,
       width = 9, height = 5, dpi = 150)

# Plot D: cumulative counts — who is growing faster?
cum_df <- yearly_set %>%
  arrange(year) %>% group_by(setting) %>%
  mutate(cum = cumsum(incidents)) %>% ungroup()

pD <- ggplot(cum_df, aes(year, cum, color = setting)) +
  geom_line(linewidth = 1) +
  scale_color_manual(values = pal) +
  labs(title = "Cumulative ESD incidents by setting",
       x = NULL, y = "Cumulative incidents", color = NULL) +
  theme(legend.position = "top")
ggsave(file.path(out, "fig10_setting_cumulative.png"), pD,
       width = 9, height = 5, dpi = 150)

# Plot E: fatalities vs non-fatal split within each setting
fat_set <- inc_y %>%
  mutate(outcome = case_when(
    fatalities > 0 ~ "Fatal",
    injuries > 0   ~ "Injury only",
    near_misses > 0 ~ "Near-miss",
    TRUE ~ "Unknown")) %>%
  count(setting, outcome)

pE <- ggplot(fat_set, aes(setting, n, fill = outcome)) +
  geom_col(position = "fill") +
  scale_y_continuous(labels = scales::percent_format(accuracy = 1)) +
  scale_fill_manual(values = c(Fatal="#c0392b", `Injury only`="#e67e22",
                               `Near-miss`="#27ae60", Unknown="#999999")) +
  labs(title = "Outcome composition by setting",
       x = NULL, y = "Share", fill = NULL)
ggsave(file.path(out, "fig11_setting_outcome_mix.png"), pE,
       width = 7, height = 4.5, dpi = 150)

cat("\nPlots saved to: ", out, "\n", sep = "")
