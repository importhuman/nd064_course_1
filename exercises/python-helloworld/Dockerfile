# Set base image
FROM python:3.8-alpine3.12
# Set label (metadata)
LABEL developer="importhuman"

# Copy from current local directory to /app directory on container 
COPY . /app
# Set working directory
WORKDIR /app
# Install dependencies
RUN pip install -r requirements.txt

# Run app
CMD ["python3", "app.py"]
