FROM python:3.9-slim

COPY . .

RUN pip install -r requirements.txt

#CMD ["python", "./src/app.py"]
CMD ["python", "app.py"]