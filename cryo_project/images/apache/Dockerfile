FROM boinc/server_apache:4.0.1-b2d

RUN mkdir /results && mkdir -m 777 /results/boinc2docker

RUN apt update && apt install -y python3 && apt install -y python3-pip && pip3 install --upgrade pip

