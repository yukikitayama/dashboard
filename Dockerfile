FROM python:3.9-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY .env .

COPY src .

CMD ["python", "app.py"]
