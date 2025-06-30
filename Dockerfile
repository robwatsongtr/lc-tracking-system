# Dockerfile
# A Dockerfile is made up of commands (instructions) that build an image step by step

# sets up python and minimal debian in the container
FROM python:3.11-slim 

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY ./app/ . 

# Expose port for FastAPI
EXPOSE 8000

# Run FastAPI with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
