# Use an official Python runtime as a parent image
FROM python:latest

# Install Python Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y binutils libproj-dev gdal-bin

# Adding backend directory to make absolute filepaths consistent across services
WORKDIR /app/backend

# Install Python dependencies
COPY ./backend/requirements /app/backend/requirements
RUN pip install -r requirements/development.txt

COPY ./backend/scripts/start.sh /
RUN sed -i 's/\r$//g' /start.sh && chmod +x /start.sh

COPY ./compose/backend/worker/start /start-worker
RUN sed -i 's/\r$//g' /start-worker
RUN chmod +x /start-worker

# Add the rest of the code
COPY ./backend /app/backend

# Make port 8000 available for the app
EXPOSE 8000
