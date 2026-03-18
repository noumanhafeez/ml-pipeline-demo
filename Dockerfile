# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create logs folder
RUN mkdir -p logs

# Default command (train model)
CMD ["python", "src/train.py"]