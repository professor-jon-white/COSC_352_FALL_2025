# app.R

library(shiny)
library(dplyr)
library(ggplot2)
library(leaflet)
library(DT)

# --- Ensure data exists ---

csv_file <- "data/processed/homicides_2021_2025.csv"

# If the processed CSV does not exist, run the scraper
if(!file.exists(csv_file)){
  message("Data file not found. Running scraper...")
  source("R/scrape_data.R")  # this should create the CSV
  if(!file.exists(csv_file)){
    stop("Scraper did not produce the expected CSV file. Check R/scrape_data.R")
  }
}

# Load the processed data
hdata <- read.csv(csv_file)

# --- Define UI ---
ui <- fluidPage(
  titlePanel("Baltimore City Homicides Dashboard (2021–2025)"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput("year", "Select Year:",
                  choices = c("All", sort(unique(hdata$year))))
    ),
    
    mainPanel(
      tabsetPanel(
        tabPanel("Overview",
                 plotOutput("yearlyPlot"),
                 plotOutput("agePlot")
        ),
        tabPanel("Map",
                 leafletOutput("map", height = "600px")
        ),
        tabPanel("Data Table",
                 DTOutput("table")
        )
      )
    )
  )
)

# --- Define server ---
server <- function(input, output, session) {
  
  filtered <- reactive({
    if (input$year == "All") return(hdata)
    hdata %>% filter(year == input$year)
  })
  
  output$yearlyPlot <- renderPlot({
    hdata %>%
      count(year) %>%
      ggplot(aes(year, n)) +
      geom_col(fill = "darkred") +
      labs(title = "Total Homicides by Year", y = "Count", x = "Year")
  })
  
  output$agePlot <- renderPlot({
    filtered() %>%
      ggplot(aes(as.numeric(age))) +
      geom_histogram(binwidth = 5, fill = "steelblue") +
      labs(title = "Age Distribution", x = "Age", y = "Frequency")
  })
  
  output$map <- renderLeaflet({
    leaflet(filtered()) %>%
      addTiles()
  })
  
  output$table <- renderDT({
    datatable(filtered(), filter = "top", options = list(pageLength = 20))
  })
}

# --- Launch app ---
shinyApp(ui, server)
