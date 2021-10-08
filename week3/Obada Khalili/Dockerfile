FROM python:3.9-slim-buster

WORKDIR /yata
COPY yata .

RUN apt-get update && apt-get install make
RUN make install

ENTRYPOINT ["make"]
CMD ["start"]
