FROM ubuntu:23.04
RUN apt-get update 
RUN apt-get install -y python3 python3-pip
RUN apt -f install -y
RUN apt-get install -y wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install ./google-chrome-stable_current_amd64.deb -y
RUN apt-get install -y git
RUN git clone https://github.com/andrew-qian/Joyces.git
WORKDIR "/Joyces"
RUN ls
RUN pip install -r requirements.txt
RUN python main.py