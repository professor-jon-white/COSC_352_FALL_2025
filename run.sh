#!/bin/bash

DOCKER_IMAGE="project4_scala_app"

# Build Docker image if not exists
if ! docker images | grep -q "$DOCKER_IMAGE"; then
    echo "Docker image not found. Building..."
    docker build -t "$DOCKER_IMAGE" .
    if [ $? -ne 0 ]; then
        echo "Error: Docker build failed"
        exit 1
    fi
fi

# Run the Docker container
docker run --rm "$DOCKER_IMAGE"
