FROM ubuntu:16.04
MAINTAINER <Mike D'Itri >

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install Numpy
RUN pip3 install pandas 
RUN pip3 install matplotlib
RUN pip3 install seaborn
RUN pip3 install tqdm
WORKDIR /app
CMD ["python3", "/app/week7_script.py","wine.data.txt"]