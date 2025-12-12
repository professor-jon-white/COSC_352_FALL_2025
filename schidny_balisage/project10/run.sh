#!/bin/bash

# Turing Machine Simulator - Easy Run Script
set -e

echo "========================================"
echo "  Turing Machine Simulator"
echo "  Project 10 - COSC 352"
echo "========================================"
echo ""

if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed."
    exit 1
fi

echo "✓ Docker is installed"
echo ""
echo "📦 Building Docker image..."
docker build -t turing-machine .

echo ""
echo "========================================"
echo "  Choose an option:"
echo "========================================"
echo "1. Run Web Interface"
echo "2. Run CLI Interface"
echo "3. Run Tests"
echo "4. Exit"
echo ""
read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo ""
        echo "🌐 Starting Web Interface..."
        echo "   Open browser to: http://localhost:5000"
        echo ""
        docker run -p 5000:5000 turing-machine
        ;;
    2)
        echo ""
        echo "💻 Starting CLI Interface..."
        docker run -it turing-machine python cli.py
        ;;
    3)
        echo ""
        echo "🧪 Running Tests..."
        docker run turing-machine python test_machines.py
        ;;
    4)
        exit 0
        ;;
    *)
        echo "Invalid choice."
        exit 1
        ;;
esac
