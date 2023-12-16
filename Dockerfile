FROM python:3.11

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y curl && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11 && \
    pip3 install --upgrade pip && \
    pip3 install django djangorestframework django-allauth django-model-utils django-otp

# Copy the application code if applicable
# COPY . /app
# WORKDIR /app

# Expose the port your application will run on
EXPOSE 80
EXPOSE 8000

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
