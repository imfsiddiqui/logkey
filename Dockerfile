# Use an official Python runtime as a parent image
FROM python:3.13.5-alpine3.22

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python", "src/logkey/logkey.py"]
