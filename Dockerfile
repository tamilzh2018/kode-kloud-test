# Use the official Node.js image as the base image
FROM node:14

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the package.json file into the container
COPY package.json /app

# Install the dependencies
RUN npm install

# Copy the server.js file into the container
COPY server.js /app

# Expose port 6100
EXPOSE 6100

# Define the command to run the server.js when the container starts
CMD ["node", "server.js"]

---
# Use a Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and source code
COPY src/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

# Expose port 3003
EXPOSE 3003

# Run the server
CMD ["python", "server.py"]

---