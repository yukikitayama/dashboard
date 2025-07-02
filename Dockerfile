FROM python:3.9-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY .env .

COPY src .

# COPY app.py .

# CMD ["python", "app.py"]

CMD ["python", "./src/app.py"]