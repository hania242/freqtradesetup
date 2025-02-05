# Use a lightweight Python image
FROM python:3.9

# Install dependencies
RUN apt-get update && apt-get install -y docker.io

# Set up working directory
WORKDIR /app

# Copy files
COPY . .

# Install Python requirements
RUN pip install flask

# Expose the web server port
EXPOSE 5000

# Run Flask server
CMD ["python", "app.py"]
