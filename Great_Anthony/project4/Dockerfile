FROM openjdk:11-slim
ARG SCALA_VERSION=2.13.12

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends curl ca-certificates; \
    curl -fsSL -o /tmp/scala.deb "https://downloads.lightbend.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.deb"; \
    dpkg -i /tmp/scala.deb || (apt-get -y -f install && dpkg -i /tmp/scala.deb); \
    rm -f /tmp/scala.deb; \
    rm -rf /var/lib/apt/lists/*; \
    apt-get clean; \
    scala -version

WORKDIR /app
COPY . /app

RUN scalac HomicideAnalysis.scala
CMD ["scala", "HomicideAnalysis"]
