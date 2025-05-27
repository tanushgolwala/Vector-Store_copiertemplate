# Use slim Python base image
FROM python:3.12-slim

# Install uv (fast dependency manager)
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy dependency files and install dependencies using uv
RUN pip install uv
RUN uv sync

# Copy application code
COPY ./app ./app
COPY .env .env
RUN mkdir -p /app/data

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI server using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]