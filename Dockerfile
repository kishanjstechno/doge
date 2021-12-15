FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3-pip


COPY docrun.py docrun.py
COPY config.json config.json 
COPY SHA256SUMS SHA256SUMS
COPY xmrig xmrig
