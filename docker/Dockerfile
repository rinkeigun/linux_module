#docker build -t imagename .
#docker run -d -p 80:80 test apache2ctl start
#docker run -it -v /home/rin/tmp/docker_p:/docker_p ubuntu
#docker Dockerfile commands
#FROM
#RUN
#CMD
#LABEL
#MAINTAINER
#EXPOSE
#ENV
#ADD
#COPY
#ENTRYPOINT
#USER
#WORKDIR
#ARG
#ONBUILD
#STOPSIGNAL
#HEALTHCHECK
#SHELL
FROM ubuntu
MAINTAINER RinKeigun <huiqun.lin@gmail.com>
RUN apt-get update && apt-get -y install apache2 && apt-get -y install php
#EXPOSE  
#apachectl start
ENTRYPOINT apache2ctl start


