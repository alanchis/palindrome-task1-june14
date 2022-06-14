FROM python:3.10-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

COPY . /app

RUN pip install -r requirements.txt

CMD ["python3", "src/app.py"]


