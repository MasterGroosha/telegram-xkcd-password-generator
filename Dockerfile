FROM python:3.8-slim-buster
WORKDIR /app
COPY wrds.txt /app/
COPY requirements.txt /app/requirements.txt
COPY other /app/other
COPY handlers /app/handlers
COPY data/config/config.example.ini /app/data/config/
RUN mkdir -p /app/data/database \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt
COPY *.py /app/
CMD ["python", "bot.py"]
