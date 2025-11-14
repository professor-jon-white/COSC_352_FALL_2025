ibrary(rvest)
library(dplyr)
library(stringr)
library(purrr)
library(tibble)

links <- c(
  "https://chamspage.blogspot.com/2021/",
  "https://chamspage.blogspot.com/2022/01/2022-baltimore-city-homicides-list.html",
  "https://chamspage.blogspot.com/2023/01/2023-baltimore-city-homicides-list.html",
  "https://chamspage.blogspot.com/2024/01/2024-baltimore-city-homicide-list.html",
  "https://chamspage.blogspot.com/2025/01/2025-baltimore-city-homicide-list.html"
)

scrape_one_year <- function(url) {
  page <- read_html(url)

  entries <- page %>% html_nodes("div") %>% html_text()

  raw <- tibble(raw = entries)

  cleaned <- raw %>%
    filter(str_detect(raw, "\\d{1,2}/\\d{1,2}/\\d{4}")) %>%
    mutate(
      date = str_extract(raw, "\\d{1,2}/\\d{1,2}/\\d{4}"),
      name = str_extract(raw, "(?<=:)\\s*[A-Za-z' -]+"),
      age = str_extract(raw, "\\d+(?=\\s*years|\\s*year)"),
      location = str_extract(raw, "Location:.*"),
      cause = str_extract(raw, "Cause:.*"),
      notes = raw
    )

  cleaned
}

all_data <- map_df(links, scrape_one_year)

all_data$year <- substr(all_data$date, 7, 10)

dir.create("data/processed", recursive = TRUE, showWarnings = FALSE)
write.csv(all_data, "data/processed/homicides_2021_2025.csv", row.names = FALSE)

print("Scraping complete. File saved to data/processed/")

