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
# Stage 1: Build React app. Uses Node.js to install dependencies and run the React build.
FROM node:18-alpine AS builder

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY . .

# Build the React app .Produces static files in /app/build.
RUN npm run build

---

# Stage 2: Serve with nginx. Uses nginx (tiny, fast web server).
FROM nginx:alpine AS production

# Copy built React files from builder stage.Copies only the built static files
COPY --from=builder /app/build /usr/share/nginx/html

# Copy custom nginx config (optional)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
