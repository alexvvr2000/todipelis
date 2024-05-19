FROM python:bookworm

WORKDIR /ApiTodiPelis

COPY ./ApiTodiPelis/setup.py setup.py
COPY ./ApiTodiPelis/requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y mariadb-client

RUN pip install .
CMD ["flask", "run", "-h", "0.0.0.0"]