FROM python:bookworm

WORKDIR /ApiTodiPelis

COPY ./ApiTodiPelis/requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y mariadb-client

COPY ./ApiTodiPelis .

RUN pip install .

CMD ["flask", "run", "-h", "0.0.0.0"]