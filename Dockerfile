FROM python:3.8-slim-buster
WORKDIR /app
COPY wrds.txt /app/
RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY other /app/other
COPY handlers /app/handlers
COPY config/config.example.ini /app/config/
COPY *.py /app/
CMD ["python", "bot.py"]
