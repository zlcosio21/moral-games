FROM python:3.14.0b1-bookworm

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# COMANDOS
# docker build -t moral-games .
# docker run -p 8000:8000 moral-games
