# Use an official Python image as the base
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port Gradio runs on
EXPOSE 7860

# Command to run the application
CMD ["python", "app.py"]
