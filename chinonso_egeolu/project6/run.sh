#!/bin/bash
# Docker image name
IMAGE_NAME="baltimore-homicide-go"

# Check if image exists, build if not
if ! docker images | grep -q "$IMAGE_NAME"; then
  echo "Building Docker image..."
  docker build -t "$IMAGE_NAME" .
  if [ $? -ne 0 ]; then
    echo "Failed to build Docker image."
    exit 1
  fi
fi

# Pass all arguments to the container
# -v mounts current directory so files can be written to host
docker run --rm -v "$(pwd):/output" "$IMAGE_NAME" "$@"