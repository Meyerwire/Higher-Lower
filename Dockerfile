FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN apt update -y
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "./webapp/app.py"]