FROM adoptopenjdk/openjdk11:alpine

WORKDIR /opt/spark

COPY spark-3.5.0-bin-hadoop3 /opt/spark

ENV SPARK_HOME=/opt/spark

ENV PATH=$PATH:$SPARK_HOME/bin

CMD ["spark-shell"]
