FROM ubuntu:23.04
ARG SENDER_EMAIL
ARG SENDER_PASSWORD
ARG RECEIVER_EMAILS
RUN apt-get update 
RUN apt-get install -y python3 python3-pip
RUN apt -f install -y
RUN apt-get install -y git
RUN git clone https://github.com/andrew-qian/Joyces.git
WORKDIR "/Joyces"
RUN ls
CMD [ "python3", "-u", "test.py" ]