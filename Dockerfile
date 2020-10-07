FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y wget

WORKDIR /app
RUN mkdir downloads wget_logs

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD autoapp.py /app/
ADD simple_downloader /app/simple_downloader

CMD ["gunicorn", "autoapp:app", "-b", "0.0.0.0:80", "--log-file", "-", "--access-logfile", "-", "--workers", "2", "--keep-alive", "0"]
