# Use the official Python image as the base
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application into the container
COPY . .

# Set the Flask app environment variable
ENV FLASK_APP=web_app.py

# Expose the port Flask will run on
EXPOSE 5000

# Start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]

