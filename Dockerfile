FROM python:3.10.6-buster

WORKDIR /prod

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install .

CMD uvicorn bestcompany.api.fast:app --host 0.0.0.0 --port $port
