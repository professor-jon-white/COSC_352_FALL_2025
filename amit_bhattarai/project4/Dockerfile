FROM hseeberger/scala-sbt:17.0.2_1.6.2_3.1.1

WORKDIR /app

# Copy Scala program and CSV (note exact filename)
COPY HomicideAnalysis.scala .
COPY Homicides.csv .

# Compile Scala program
RUN scalac HomicideAnalysis.scala

# Run the program
CMD ["scala", "HomicideAnalysis"]
