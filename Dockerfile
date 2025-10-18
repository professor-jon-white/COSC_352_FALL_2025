<<<<<<< HEAD
FROM eclipse-temurin:21-jdk AS build
RUN apt-get update && apt-get install -y curl gzip && rm -rf /var/lib/apt/lists/*
RUN curl -L -s https://github.com/VirtusLab/scala-cli/releases/download/v1.5.3/scala-cli-x86_64-pc-linux.gz \
  | gunzip > /usr/local/bin/scala-cli && chmod +x /usr/local/bin/scala-cli
WORKDIR /app
COPY src ./src
RUN scala-cli --power package src/Main.scala --assembly -o app.jar

FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=build /app/app.jar /app/app.jar
ENTRYPOINT ["java","-jar","/app/app.jar"]
=======
# Use OpenJDK base image with JDK for compilation
FROM openjdk:11-jdk-slim

# Install Scala
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://downloads.lightbend.com/scala/2.13.12/scala-2.13.12.tgz && \
    tar -xzf scala-2.13.12.tgz && \
    mv scala-2.13.12 /usr/local/scala && \
    rm scala-2.13.12.tgz && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set Scala environment variables
ENV SCALA_HOME=/usr/local/scala
ENV PATH=$PATH:$SCALA_HOME/bin

# Set working directory
WORKDIR /app

# Copy the Scala source file
COPY BaltimoreHomicideAnalysis.scala .

# Compile the Scala program
RUN scalac BaltimoreHomicideAnalysis.scala

# Default command (will be overridden by # Use OpenJDK base image with JDK for compilation
FROM openjdk:11-jdk-slim

# Install Scala
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://downloads.lightbend.com/scala/2.13.12/scala-2.13.12.tgz && \
    tar -xzf scala-2.13.12.tgz && \
    mv scala-2.13.12 /usr/local/scala && \
    rm scala-2.13.12.tgz && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set Scala environment variables
ENV SCALA_HOME=/usr/local/scala
ENV PATH=$PATH:$SCALA_HOME/bin

# Set working directory
WORKDIR /app

# Copy the Scala source file
COPY BaltimoreHomicideAnalysis.scala .

# Compile the Scala program
RUN scalac BaltimoreHomicideAnalysis.scala

# Default command (will be overridden by run.sh)
CMD ["scala", "BaltimoreHomicideAnalysis"]run.sh)
CMD ["scala", "BaltimoreHomicideAnalysis"
>>>>>>> c34828076555855b1b9de7e76535747aa9c1b01b
