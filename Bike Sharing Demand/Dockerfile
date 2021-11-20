FROM python:3.9-slim-buster

WORKDIR /app
COPY app .

RUN apt-get update && apt-get install make
RUN make install

CMD ["make", "start"]
