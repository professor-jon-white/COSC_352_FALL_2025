#!/bin/bash

# Parse command line arguments
OUTPUT_FORMAT="stdout"

for arg in "$@"; do
  case $arg in
    --output=*)
      OUTPUT_FORMAT="${arg#*=}"
      shift
      ;;
    *)
      ;;
  esac
done

# Compile the Scala program
echo "Compiling Scala program..."
scalac HomicideAnalysis.scala

# Run the Scala program with the output format
echo "Running analysis with output format: $OUTPUT_FORMAT"
scala HomicideAnalysis "$OUTPUT_FORMAT"
