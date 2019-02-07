# Use an official Python runtime as a parent image
FROM php:7.0-apache
FROM python

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 150

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "index.py"]

