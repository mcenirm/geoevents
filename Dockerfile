FROM python:2.7.9

RUN apt-get update
RUN apt-get autoremove -y

RUN apt-get install -y --no-install-recommends python-gdal
RUN rm -rf /var/lib/apt/lists/*

COPY geoevents/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY *.patch /tmp/
RUN cd /usr/local/lib/python2.7/site-packages && cat /tmp/*.patch | patch -p1

RUN mkdir -p /usr/src/app
COPY . /usr/src/app

WORKDIR /usr/src/app

EXPOSE 8000
CMD ["paver", "start"]
