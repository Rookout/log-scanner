FROM python:3.7

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "index.py"]