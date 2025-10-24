#!/bin/bash

echo "Setting up Project 5..."

# Create data directory if it doesn't exist
mkdir -p data

# Check if we need to download the data
if [ ! -f "data/homicide-data.csv" ]; then
    echo "Downloading homicide data..."
    wget -O data/homicide-data.csv https://raw.githubusercontent.com/washingtonpost/data-homicides/master/homicide-data.csv 2>/dev/null || echo "Please add your data file manually"
fi

echo "Setup complete!"
