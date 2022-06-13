FROM python:3.7.9

ENV CERT_MOZILLA_URL https://curl.haxx.se/ca/cacert.pem
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
ENV PYTHONPATH /opt/app

# install "software-properties-common" (for the "add-apt-repository")
RUN apt-get update \
&& apt-get install -y software-properties-common

# add the "JAVA" repository
RUN apt-add-repository -y \
    'deb http://security.debian.org/debian-security stretch/updates main'

# install OpenJDK-8
RUN apt-get update \
&& apt-get install -y openjdk-8-jdk \
&& apt-get install -y ant \
&& apt-get clean

# fix certificate issues
RUN apt-get update \
&& apt-get install ca-certificates-java \
&& apt-get clean \
&& update-ca-certificates -f

# install other dependencies
RUN apt-get update \
&&  apt-get install -y wget telnet \
&&  rm -rf /var/lib/apt/lists/* \
&&  rm -rf /var/cache/* \
&&  mkdir -p /etc/pki/tls/certs \
&&  mkdir -p /opt/app/jars \
&&  wget $CERT_MOZILLA_URL -O /etc/pki/tls/certs/ca-bundle.crt 

COPY . /opt/app/
WORKDIR /opt/app/

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "/bin/bash" ]
