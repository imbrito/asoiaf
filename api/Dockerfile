FROM python:3.7

ENV CERT_MOZILLA_URL https://curl.haxx.se/ca/cacert.pem
ENV PYTHONPATH /opt/app

# install other dependencies
RUN apt-get update \
&&  apt-get install -y wget telnet \
&&  rm -rf /var/lib/apt/lists/* \
&&  rm -rf /var/cache/* \
&&  mkdir -p /etc/pki/tls/certs \
&&  wget $CERT_MOZILLA_URL -O /etc/pki/tls/certs/ca-bundle.crt 

COPY . /opt/app/
WORKDIR /opt/app

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_ENV development

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["flask","run"]