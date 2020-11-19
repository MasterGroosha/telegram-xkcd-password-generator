FROM python:3.8-slim-buster
WORKDIR /app
COPY vocabulary.txt /app/
COPY docker-entrypoint.sh /app/
RUN chmod +x docker-entrypoint.sh && pip install --no-cache-dir --upgrade pip
COPY requirements.txt /app/requirements.txt
COPY config/config.example.ini /app/config/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY other /app/other
COPY handlers /app/handlers
COPY *.py /app/
CMD ["./docker-entrypoint.sh"]
