FROM python:3.9.1

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

COPY ./requirements.txt /app/requirements.txt
COPY ./app.py /app/app.py
COPY templates /app/templates

WORKDIR /app

RUN pip install -r /app/requirements.txt

CMD [ "python", "./app.py" ]

