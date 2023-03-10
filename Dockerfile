FROM python:3.9-slim

WORKDIR /app

COPY ./ /app
COPY ./requirements.txt /app

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host=0.0.0.0", "--reload"]
