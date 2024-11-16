# Use an official Python image for version 3.9
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Jupyter Lab
RUN pip install jupyterlab

# Expose the Jupyter default port
EXPOSE 8888

# Define the default command to run Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root"]

# docker build -t gold-price-prediction .
# docker run -p 8888:8888 gold-price-prediction
