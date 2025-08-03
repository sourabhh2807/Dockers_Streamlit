# Use the official Python image from Docker Hub
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the current directory into the container's /app folder
COPY . /app

# Install the dependencies listed in requirements.txt
RUN pip install -v --no-cache-dir -r requirements.txt

# Expose port 8501, which Streamlit uses by default
EXPOSE 8501

# Define the command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
