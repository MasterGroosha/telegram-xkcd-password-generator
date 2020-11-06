FROM python:3.8-slim-buster
WORKDIR /app
COPY wrds.txt /app/
COPY requirements.txt /app/requirements.txt
COPY lang /app/lang
COPY keyboards /app/keyboards
COPY handlers /app/handlers
COPY config/config.example.ini /app/config/
RUN mkdir -p /app/database \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt
COPY *.py /app/
CMD ["python", "bot.py"]
