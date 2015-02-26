FROM python:2.7.9

RUN apt-get update
RUN apt-get autoremove -y

RUN apt-get install -y --no-install-recommends python-gdal
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app
COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r geoevents/requirements.txt

EXPOSE 8000
CMD ["paver", "start"]
