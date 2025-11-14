FROM rocker/shiny:latest

RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev libssl-dev libxml2-dev libgeos-dev \
    && rm -rf /var/lib/apt/lists/*

RUN R -e "install.packages(c('shiny','dplyr','ggplot2','leaflet','rvest','DT','stringr','purrr','tibble'))"

COPY . /srv/shiny-server/homicides/
WORKDIR /srv/shiny-server/homicides/

EXPOSE 3838
CMD ["/usr/bin/shiny-server"]

