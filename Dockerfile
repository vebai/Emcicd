# Use an official Python runtime image
FROM python:2.7-slim

# create and set working directory
ADD . /app
WORKDIR /app

# Copy application files to container working directory
COPY ./app.py ./app
COPY ./flights.csv ./app

# Run app.py when the container launches

CMD ["python", "app.py"]