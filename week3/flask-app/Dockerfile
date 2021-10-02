FROM python:3.8-slim-buster

WORKDIR /app

COPY app/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app/src .

EXPOSE 8081

CMD [ "python", "main.py"]