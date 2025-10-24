# Project 5: Multi-Format Output for Crime Data Analysis

## Overview
This project extends Project 4 by adding support for multiple output formats (CSV and JSON) in addition to the default stdout output.

## Data Format Choices

### CSV Format
I chose CSV (Comma-Separated Values) for the following reasons:
- **Universal Compatibility**: CSV files can be opened in Excel, Google Sheets, and most data analysis tools
- **Human Readable**: Easy to read and edit in text editors
- **Lightweight**: Minimal overhead compared to other formats
- **Standard Format**: Widely used for tabular data in data science and analytics

### JSON Format
I chose JSON (JavaScript Object Notation) for the following reasons:
- **Web-Friendly**: Native format for web APIs and JavaScript applications
- **Structured Data**: Supports nested data structures and complex relationships
- **Machine Readable**: Easy to parse programmatically in virtually any programming language
- **Future-Proof**: Ideal for integration with modern web services and databases

## Usage

### Run with default output (stdout):
```bash
./run.sh
```

### Run with CSV output:
```bash
./run.sh --output=csv
```
This creates an `output.csv` file with the analysis results.

### Run with JSON output:
```bash
./run.sh --output=json
```
This creates an `output.json` file with the analysis results.

## Docker Support

### Build the Docker image:
```bash
docker build -t homicide-analysis .
```

### Run with Docker (stdout):
```bash
docker run homicide-analysis
```

### Run with Docker (CSV output):
```bash
docker run homicide-analysis ./run.sh --output=csv
```

### Run with Docker (JSON output):
```bash
docker run homicide-analysis ./run.sh --output=json
```

## File Structure
```
project5/
├── HomicideAnalysis.scala  # Main Scala program with multi-format output
├── run.sh                  # Shell script with flag parsing
├── Dockerfile              # Docker configuration
├── .gitignore             # Git ignore file
├── README.md              # This file
└── data/                  # Crime data directory (if needed)
```

## Requirements Met
- ✅ Continues from Project 4
- ✅ Supports CSV output format
- ✅ Supports JSON output format
- ✅ Flag-based output selection via run.sh
- ✅ Default stdout output when no flag provided
- ✅ Dockerized for consistent execution
- ✅ README explaining format choices
