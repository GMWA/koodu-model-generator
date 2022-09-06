FROM python:3.8-slim-buster

RUN addgroup --system app && adduser --system app --ingroup app

ENV APP_HOME=/home/todo
RUN mkdir $APP_HOME
RUN chmod 777 $APP_HOME
WORKDIR $APP_HOME

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV FLASK_APP=server.py

COPY . $APP_HOME

CMD [ "python3", "main.py"]