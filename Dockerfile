FROM python:3

RUN pip install -U pip \
  && pip install flask \
  && pip install gunicorn \
  && pip install docker \
  && pip install flask-sqlalchemy \
  && pip install docker-compose \
  && pip install sqlalchemy \
  && pip install sqlalchemy_utils \
  && pip install passlib \
  && pip install psycopg2


COPY . /app
WORKDIR /app

RUN pip install -e .

RUN mkdir -p /tmp/cache
ENV FLASK_APP=wedding_site.wedding_site
EXPOSE ${PORT}
WORKDIR /app/wedding_site

CMD ["gunicorn", "-c", "/app/gunicorn.conf", "wedding_site.app:app", "--log-level=info", "--reload"]
