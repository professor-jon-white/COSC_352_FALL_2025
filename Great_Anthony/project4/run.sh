#!/bin/bash

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}Baltimore Homicide Analysis - Project 4${NC}"
echo "========================================"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo -e "${RED}Error: Docker is not installed${NC}"
    exit 1
fi

# Build the Docker image if it doesn't exist or force rebuild
IMAGE_NAME="baltimore-homicide-analysis"
if [[ "$(docker images -q $IMAGE_NAME 2> /dev/null)" == "" ]]; then
    echo -e "${GREEN}Building Docker image...${NC}"
    docker build -t $IMAGE_NAME . || {
        echo -e "${RED}Failed to build Docker image${NC}"
        exit 1
    }
else
    echo -e "${GREEN}Docker image already exists${NC}"
fi

# Run the container
echo -e "${GREEN}Running analysis...${NC}"
echo ""
docker run --rm --network=host $IMAGE_NAME || {
    echo -e "${RED}Failed to run analysis${NC}"
    exit 1
}
