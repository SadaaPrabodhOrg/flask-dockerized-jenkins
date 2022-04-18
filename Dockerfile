FROM python:3.6
COPY .  /app
WORKDIR /app
Run pip install --upgrade pip==9.0.1
RUN pip3 install -r requirements.txt
# make port 8000 available to the world outside
EXPOSE 8000

CMD ["gunicorn", "--config", "./conf/gunicorn_config.py", "src.wsgi:app"]
