FROM python

WORKDIR /app
RUN mkdir downloads wget_logs

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD simple_downloader /app

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80", "--log-file", "-", "--access-logfile", "-", "--workers", "2", "--keep-alive", "0"]
