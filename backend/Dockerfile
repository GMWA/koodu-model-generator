FROM python:3.8-slim-buster

RUN addgroup --system app && adduser --system app --ingroup app

ENV APP_HOME=/home/code
RUN mkdir $APP_HOME
RUN chmod 777 $APP_HOME
WORKDIR $APP_HOME

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . $APP_HOME

EXPOSE 8000

CMD [ "uvicorn", "modelgenerator.server:app", "--reload" "--host 0.0.0.0", "--port 8000"]