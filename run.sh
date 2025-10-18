#!/bin/bash

DOCKER_IMAGE="project4_scala_app"

if ! docker images | grep -q "$DOCKER_IMAGE"; then
    echo "Docker image not found. Building..."
    docker build -t "$DOCKER_IMAGE" .
    echo "Docker image built successfully!"
fi

echo "Running analysis..."
docker run --rm "$DOCKER_IMAGE"
