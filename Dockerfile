FROM python:3

WORKDIR /usr/src/app

COPY ./app .

RUN apt update -y
RUN pip3 install -r requirements.txt

EXPOSE 5001

CMD ["python3", "./app/app.py"]