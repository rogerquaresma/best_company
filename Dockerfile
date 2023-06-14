FROM python:3.10-slim

EXPOSE 8080
WORKDIR /prod

RUN pip install --upgrade pip

COPY . .
RUN pip install -r requirements.txt

#ENV PORT 8080
#EXPOSE 8080

CMD uvicorn bestcompany.api.fast:app --host 0.0.0.0 --port 8080
