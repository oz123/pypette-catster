FROM docker.io/library/python:3.13-slim
LABEL maintainer="Oz Tiram <oz.tiram@gmail.com>"

ARG VERSION=
RUN apt-get update && apt-get install -y -qq gcc libev-dev
WORKDIR /usr/src

COPY dist/catster-${VERSION}.tar.gz /usr/src/
COPY static /usr/src/static/
COPY views /usr/src/views/
ADD requirements.txt /usr/src/
ADD docker/server.py /usr/src/
ADD pypette.py /usr/src/
RUN python3 -m pip install catster-${VERSION}.tar.gz 
RUN python3 -m pip install -r requirements.txt


ENV PATH=/usr/src/.venv/bin:$PATH

CMD ["python3", "-u", "server.py"]
