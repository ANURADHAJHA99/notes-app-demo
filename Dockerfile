FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

RUN apt-get update && apt-get install -y gcc

COPY requirements.py requirements.py

RUN pip install --no-cache-dir -r requirements.py

COPY . .

EXPOSE 8000

ENV NAME World

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "notes_project.wsgi:application"]
