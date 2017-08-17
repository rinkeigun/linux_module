FROM ubuntu
MAINTAINER RinKeigun <huiqun.lin@gmail.com>
RUN apt-get update && apt-get -y install apt-utils \
                   && apt-get -y install sqlite3 \
                   && apt-get -y install apache2 \
                   && apt-get -y install ruby \
                   && apt-get -y install imagemagick \
                   && apt-get -y install wget
RUN wget http://www.redmine.org/releases/redmine-3.4.2.tar.gz \
                   && tar xvf redmine-3.4.2.tar.gz \
                   && mv redmine-3.4.2 /var/lib/redmine \
                   && echo "production:" > /var/lib/redmine/config/database.yml \
                   && echo "  adapter: sqlite3" >> /var/lib/redmine/config/database.yml \
                   && echo "  database: db/redmine.sqlite3" >> /var/lib/redmine/config/database.yml \
                   && apt-get -y install bundler 
#docker run -it -v /media/sf_vmware-share/:/rin ubuntu /bin/sh 

#=====================================================
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
