# Use official Scala image
FROM openjdk:17-slim

# Install Scala and basic tools
RUN apt-get update && apt-get install -y scala curl && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy Scala source
COPY HomicideAnalysis.scala .

# Compile Scala program
RUN scalac HomicideAnalysis.scala

# Run the program
CMD ["scala", "HomicideAnalysis"]
