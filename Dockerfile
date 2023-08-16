# Use an official Python runtime as a parent image
FROM locustio/locust

USER root
RUN apt-get update
RUN apt-get install -y jq vim procps less

WORKDIR /app

RUN mkdir /app/locustfiles

COPY locustfiles /app/locustfiles
COPY start_worker.sh /start_worker.sh

RUN mkdir /app/reports
RUN chmod 777 /app/reports
RUN chmod 755 /start_workers.sh

EXPOSE 8089

# ENTRYPOINT [ "/bin/sh", "-c", "trap : TERM INT; sleep infinity & wait" ]
ENTRYPOINT locust --master -f $TEST_FILE
