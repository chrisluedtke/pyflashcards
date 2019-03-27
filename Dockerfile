FROM python

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

RUN flask db init && \
    flask db migrate -m "initialize database" && \
    flask db upgrade

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
