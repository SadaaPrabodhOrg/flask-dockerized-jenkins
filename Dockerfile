FROM python:3.6
COPY .  /app
WORKDIR /app
#RUN pip install --upgrade pip==20.2.2
RUN pip install --upgrade pip==20.2.2
#RUN pip install --upgrade pip==1.4
RUN pip3 install -r requirements.txt
# make port 8000 available to the world outside
EXPOSE 8000

CMD ["gunicorn", "--config", "./conf/gunicorn_config.py", "src.wsgi:app"]
