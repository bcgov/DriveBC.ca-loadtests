# Use an official Python runtime as a parent image
FROM locustio/locust

USER root
RUN apt-get update
RUN apt-get install -y jq vim procps less curl

WORKDIR /app

RUN mkdir /app/common
RUN mkdir /app/locustfiles
RUN mkdir /app/data

COPY common /app/common
COPY locustfiles /app/locustfiles
COPY data /app/data
COPY start_worker.sh /start_worker.sh

RUN mkdir /app/reports
RUN chmod 777 /app/reports
RUN chmod 755 /start_worker.sh

EXPOSE 8089

# ENTRYPOINT [ "/bin/sh", "-c", "trap : TERM INT; sleep infinity & wait" ]
ENTRYPOINT locust --master -f $TEST_FILE --loglevel WARNING
