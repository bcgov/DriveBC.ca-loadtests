# Use an official Python runtime as a parent image
FROM python:latest

# Install Python Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y binutils libproj-dev gdal-bin

# Adding backend directory to make absolute filepaths consistent across services
WORKDIR /app/backend

# Install Python dependencies
COPY ./requirements /app/backend/requirements
RUN pip install -r requirements/development.txt

COPY ./scripts/start.sh /
RUN sed -i 's/\r$//g' /start.sh && chmod +x /start.sh

# Add the rest of the code
COPY . /app/backend

# Make port 8000 available for the app
EXPOSE 8000
