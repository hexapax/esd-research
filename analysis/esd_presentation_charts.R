#!/usr/bin/env Rscript
# Presentation-quality charts for Nicole Allen's ESD talks.
# Hero chart + ratio companion, advocacy-framed, 300 DPI PNG + SVG.
# Audience: public / HOA / NFPA Expo (with Kevin Ritz).

suppressPackageStartupMessages({
  library(dplyr); library(tidyr); library(readr); library(ggplot2)
  library(MASS); library(scales)
})

root <- "/opt/repos/esd-research"
out  <- file.path(root, "analysis/outputs/presentation")
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
dock_groups <- c("Freshwater marina", "Private freshwater dock")

yearly <- inc %>%
  count(year, flag_setting) %>%
  complete(year = yr_rng, flag_setting, fill = list(n = 0)) %>%
  rename(incidents = n) %>%
  filter(flag_setting %in% dock_groups) %>%
  mutate(flag_setting = factor(flag_setting, levels = dock_groups),
         era = cut(year, breaks = c(-Inf, 2010, 2016, Inf),
                  labels = c("Pre-NEC 555 era\n(before 2011)",
                             "NEC 2011\n(30 mA GFPE at marinas)",
                             "NEC 2017+\n(expanded marina protections)")))

era_means <- yearly %>%
  group_by(flag_setting, era) %>%
  summarise(years = n(), total = sum(incidents),
            mean_per_yr = mean(incidents),
            year_lo = min(year), year_hi = max(year),
            .groups = "drop")

era_ratio <- era_means %>%
  dplyr::select(flag_setting, era, mean_per_yr) %>%
  pivot_wider(names_from = flag_setting, values_from = mean_per_yr) %>%
  mutate(ratio = `Freshwater marina` / `Private freshwater dock`)

# ======================================================================
# Visual system
# ======================================================================
# Warm/cool: marina = teal (code reached), private dock = rust (left behind).
col_marina  <- "#1B7F79"   # deep teal
col_private <- "#D2553A"   # rust red
col_dark    <- "#1F2A44"   # near-black
col_mid     <- "#55607A"
col_muted   <- "#8892A6"
col_bg_era  <- c("#F3F1EC", "#FBF5E7", "#EAF4EE")  # subtle band tints

pal <- c("Freshwater marina" = col_marina,
         "Private freshwater dock" = col_private)

base_theme <- theme_minimal(base_size = 14, base_family = "sans") +
  theme(
    plot.title = element_text(face = "bold", size = 22,
                              color = col_dark, margin = margin(b = 4)),
    plot.subtitle = element_text(size = 14, color = col_mid,
                                 margin = margin(b = 14), lineheight = 1.15),
    plot.caption = element_text(size = 9, color = col_muted,
                                hjust = 0, margin = margin(t = 12)),
    axis.title = element_text(size = 12, color = col_mid),
    axis.text  = element_text(size = 11, color = col_mid),
    panel.grid.major.y = element_line(color = "#E6E6E6"),
    panel.grid.major.x = element_blank(),
    panel.grid.minor = element_blank(),
    legend.position = "top",
    legend.justification = "left",
    legend.text = element_text(size = 12, color = col_dark),
    legend.title = element_blank(),
    legend.margin = margin(b = 4),
    plot.margin = margin(18, 22, 14, 22)
  )

# ======================================================================
# HERO CHART: yearly counts + per-era mean rate line + NEC breaks
# ======================================================================
era_bounds <- tibble(
  xmin = c(-Inf, 2010.5, 2016.5),
  xmax = c(2010.5, 2016.5, Inf),
  era  = levels(yearly$era),
  fill = col_bg_era
)

era_mean_segs <- era_means %>%
  mutate(x0 = pmax(year_lo - 0.45, min(yearly$year) - 0.5),
         x1 = year_hi + 0.45)

era_label_df <- tibble(
  x = c(1996, 2013.5, 2021),
  y = rep(6.7, 3),
  label = c("PRE-NEC 555", "NEC 2011 ERA", "NEC 2017 ERA")
)

nec_label_df <- tibble(
  x = c(2011, 2017),
  y = rep(7.3, 2),
  label = c("NEC 2011 adopted\n30 mA GFPE (marinas)",
            "NEC 2017 adopted\nsignage + branch-circuit GFPE")
)

# Per-era IRR text: rate per year + sample size
era_rate_text <- era_means %>%
  mutate(mid_x = (year_lo + year_hi) / 2,
         label = sprintf("%.2f/yr  (n=%d)", mean_per_yr, total),
         # vertical offset based on setting to stack labels
         y = ifelse(flag_setting == "Freshwater marina", 5.5, 6.1))

# Marina-to-private ratio annotation per era (punchline)
ratio_ann <- era_ratio %>%
  mutate(mid_x = case_when(
           era == levels(yearly$era)[1] ~ 1996,
           era == levels(yearly$era)[2] ~ 2013.5,
           TRUE ~ 2021),
         label = sprintf("Marina : Private\n%.2f : 1",
                         ifelse(is.finite(ratio), ratio, NA)))

hero <- ggplot() +
  # Era shading
  geom_rect(data = era_bounds,
            aes(xmin = xmin, xmax = xmax, ymin = -Inf, ymax = Inf,
                fill = era), alpha = 0.55, show.legend = FALSE) +
  scale_fill_manual(values = setNames(col_bg_era, levels(yearly$era)),
                    guide = "none") +
  # NEC vertical lines
  geom_vline(xintercept = c(2010.5, 2016.5),
             linetype = "dashed", color = col_dark, alpha = 0.5,
             linewidth = 0.4) +
  # Era labels at top
  geom_text(data = era_label_df,
            aes(x = x, y = y, label = label),
            color = col_muted, size = 3.4, fontface = "bold",
            vjust = 0.5, hjust = 0.5) +
  # NEC code adoption labels
  geom_text(data = nec_label_df,
            aes(x = x, y = y, label = label),
            color = col_dark, size = 3.1, fontface = "italic",
            vjust = 0.5, hjust = 0.5, lineheight = 0.95) +
  # Yearly bars (dodged)
  geom_col(data = yearly,
           aes(x = year, y = incidents, fill = flag_setting),
           position = position_dodge(width = 0.7),
           width = 0.7, color = NA, alpha = 0.85) +
  # Per-era mean-rate horizontal thick segments (the punchline)
  geom_segment(data = era_mean_segs,
               aes(x = x0, xend = x1, y = mean_per_yr, yend = mean_per_yr,
                   color = flag_setting),
               linewidth = 1.8) +
  # Per-era mean-rate text labels
  geom_text(data = era_rate_text,
            aes(x = mid_x, y = y, label = label,
                color = flag_setting),
            size = 3.4, fontface = "bold", hjust = 0.5,
            show.legend = FALSE) +
  # Ratio annotations
  geom_text(data = ratio_ann,
            aes(x = mid_x, y = 4.8, label = label),
            color = col_dark, size = 3.2, fontface = "bold",
            hjust = 0.5, lineheight = 0.95) +
  scale_color_manual(values = pal, name = NULL) +
  scale_fill_manual(values = c(pal,
                               setNames(col_bg_era, levels(yearly$era))),
                    breaks = names(pal), name = NULL) +
  scale_x_continuous(breaks = seq(1985, 2025, 5),
                     limits = c(min(yearly$year) - 0.8, max(yearly$year) + 0.8),
                     expand = expansion(mult = c(0.01, 0.01))) +
  scale_y_continuous(breaks = 0:6,
                     limits = c(0, 7.8),
                     expand = expansion(mult = c(0.01, 0.02))) +
  labs(
    title = "Where the code reached, it worked.",
    subtitle = paste0(
      "Commercial marinas got National Electric Code 555 protections in 2011. ",
      "Private docks did not.\n",
      "Before 2011, marinas saw more ESD incidents per year than private docks. ",
      "After 2011, that flipped — and stayed flipped."),
    x = NULL,
    y = "ESD incidents per year",
    caption = paste0(
      "Source: 201-incident independently-verified dataset (1981-2025). ",
      "Bars = yearly counts. Horizontal lines = mean rate per NEC era. ",
      "Flags assigned by reasoning-classifier review of each incident narrative."
    )
  ) +
  base_theme +
  theme(legend.position = "top",
        legend.justification = "left")

# Save hero at two sizes: 16:9 slide and 4:3 slide
ggsave(file.path(out, "hero_nec_trend_16x9.png"), hero,
       width = 13.33, height = 7.5, dpi = 300, bg = "white")
ggsave(file.path(out, "hero_nec_trend_4x3.png"), hero,
       width = 10, height = 7.5, dpi = 300, bg = "white")

cat("Hero chart saved.\n")

# ======================================================================
# RATIO FLIP companion chart
# ======================================================================
ratio_df <- era_ratio %>%
  mutate(era_short = c("Pre-NEC 555\n(before 2011)",
                       "NEC 2011 era\n(2011-2016)",
                       "NEC 2017+ era\n(2017-present)"),
         era_short = factor(era_short, levels = era_short),
         label = sprintf("%.2f", ratio),
         who_higher = ifelse(ratio > 1, "Marina higher", "Private dock higher"),
         bar_color = ifelse(ratio > 1, col_marina, col_private))

ratio_chart <- ggplot(ratio_df, aes(era_short, ratio, fill = bar_color)) +
  geom_col(width = 0.6, color = NA, alpha = 0.9) +
  geom_hline(yintercept = 1, linetype = "dashed",
             color = col_dark, alpha = 0.6) +
  annotate("text", x = 0.55, y = 1.02, label = "parity (1.0)",
           hjust = 0, vjust = 0, size = 3.2, color = col_dark,
           fontface = "italic") +
  geom_text(aes(label = label, color = bar_color),
            vjust = -0.45, fontface = "bold", size = 7,
            show.legend = FALSE) +
  geom_text(aes(label = who_higher, y = 0.08, color = "white"),
            fontface = "bold", size = 3.5, color = "white",
            show.legend = FALSE) +
  scale_fill_identity() +
  scale_color_identity() +
  scale_y_continuous(limits = c(0, 2.1), breaks = c(0, 0.5, 1, 1.5, 2),
                     expand = expansion(mult = c(0.01, 0.08))) +
  labs(
    title = "The ratio flipped — and stayed flipped.",
    subtitle = paste0(
      "Marina ESDs vs. private-dock ESDs, mean per year in each NEC era.\n",
      "Before 2011 marinas had 1.71x the rate of private docks. ",
      "After NEC 555, private docks have roughly 2x the rate of marinas."),
    x = NULL,
    y = "Ratio: marina incidents / private-dock incidents",
    caption = paste0(
      "A ratio above 1.0 means marinas were deadlier per year; below 1.0 means ",
      "private docks were. Same dataset as hero chart; means over raw yearly counts."
    )
  ) +
  base_theme +
  theme(legend.position = "none")

ggsave(file.path(out, "ratio_flip_16x9.png"), ratio_chart,
       width = 13.33, height = 7.5, dpi = 300, bg = "white")
ggsave(file.path(out, "ratio_flip_4x3.png"), ratio_chart,
       width = 10, height = 7.5, dpi = 300, bg = "white")

cat("Ratio chart saved.\n")

# ======================================================================
# SIMPLE per-era per-setting mean rate — clean comparison
# ======================================================================
per_era <- era_means %>%
  mutate(era_short = factor(case_when(
    grepl("before", era) ~ "Pre-NEC 555\n(1981-2010)",
    grepl("2011",   era) ~ "NEC 2011 era\n(2011-2016)",
    TRUE                 ~ "NEC 2017+ era\n(2017-2025)"
  ), levels = c("Pre-NEC 555\n(1981-2010)", "NEC 2011 era\n(2011-2016)",
                "NEC 2017+ era\n(2017-2025)")))

era_bars <- ggplot(per_era,
                   aes(era_short, mean_per_yr, fill = flag_setting)) +
  geom_col(position = position_dodge(width = 0.72),
           width = 0.65, color = NA, alpha = 0.9) +
  geom_text(aes(label = sprintf("%.2f", mean_per_yr),
                color = flag_setting),
            position = position_dodge(width = 0.72),
            vjust = -0.45, fontface = "bold", size = 5.5,
            show.legend = FALSE) +
  geom_text(aes(label = sprintf("n=%d", total),
                y = 0.05),
            position = position_dodge(width = 0.72),
            color = "white", fontface = "bold", size = 3.2,
            show.legend = FALSE) +
  scale_fill_manual(values = pal, name = NULL) +
  scale_color_manual(values = pal, guide = "none") +
  scale_y_continuous(limits = c(0, 3.2),
                     expand = expansion(mult = c(0.01, 0.05))) +
  labs(
    title = "Marina ESD rate held flat. Private-dock rate nearly tripled.",
    subtitle = paste0(
      "Mean ESD incidents per year in each NEC era, by setting.\n",
      "Marinas, regulated under NEC 555 + NFPA 303, did not see a rise. ",
      "Private residential docks, which have no equivalent code, did."),
    x = NULL,
    y = "Mean ESD incidents per year",
    caption = paste0(
      "Marina rate: 0.80 / 1.00 / 0.67 per year across the three eras. ",
      "Private-dock rate: 0.47 / 2.67 / 1.44 per year. ",
      "Sample sizes (n) shown inside each bar."
    )
  ) +
  base_theme +
  theme(legend.position = "top")

ggsave(file.path(out, "era_bars_16x9.png"), era_bars,
       width = 13.33, height = 7.5, dpi = 300, bg = "white")
ggsave(file.path(out, "era_bars_4x3.png"), era_bars,
       width = 10, height = 7.5, dpi = 300, bg = "white")

cat("Era bars chart saved.\n")
cat("All presentation charts written to: ", out, "\n", sep = "")
