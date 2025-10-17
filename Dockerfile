FROM hseeberger/scala-sbt:17.0.2_1.6.2_3.1.1

WORKDIR /app

COPY HomicideAnalysis.scala .
COPY homicides.csv .

RUN scalac HomicideAnalysis.scala

CMD ["scala", "HomicideAnalysis"]
