FROM hseeberger/scala-sbt:17.0.2_1.6.2_3.1.1

WORKDIR /app

# Copy Scala program only
COPY HomicideAnalysis.scala .

# Compile Scala program
RUN scalac HomicideAnalysis.scala

# Run the program
CMD ["scala", "HomicideAnalysis"]
