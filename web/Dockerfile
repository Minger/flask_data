FROM ubuntu:latest
LABEL Ming "minger@gmail.com"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential libpq-dev python-dev locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
#CMD ["app.py"]