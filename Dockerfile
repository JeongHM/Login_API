FROM ubuntu:16.04

WORKDIR /home

RUN apt-get update \
    && apt-get install -y software-properties-common \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y python3.7

RUN unlink /usr/bin/python3 \
    && ln -s /usr/bin/python3.7 /usr/bin/python3 \
    && apt-get install -y python3-pip

RUN apt-get install curl \
    && curl -sL https://deb.nodesource.com/setup_12.x | bash - \
    && apt-get install -y nodejs

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "application.py"]