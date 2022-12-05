# Solution for Problem Set 5 Question 2

pacman::p_load(dplyr, ggplot2)

# Load data
df <- readxl::read_excel(
    "PS5_data.xlsx", 
    skip=2,
    col_names=c("duration", "heart_rate")
)

# Fit the linear model
fit <- lm(heart_rate ~ duration, data=df)
print(summary(fit))

# Plot the fit
p <- df %>%
    ggplot(aes(x=duration, y=heart_rate)) +
        geom_point(size=2.5) +
        geom_smooth(
            method="lm", 
            formula=y~x,
            color="red", 
            fill="#db8e88"
        ) +
        ggpubr::stat_regline_equation(
            aes(label=paste(..eq.label.., ..adj.rr.label.., sep="~~~~")),
        ) +
        labs(
            title="Determination of Maximum Heart Rate by Treadmill Time",
            x="Duration (s)",
            y="Heart Rate (BPM)"
        ) +
        ggpubr::theme_pubr() +
        theme(
            plot.title=element_text(hjust=0.5, size=14),
            axis.title=element_text(size=12),
            axis.text=element_text(size=11)
        )
ggsave("PS5_fit.png", p, width=7, height=4, dpi=300)