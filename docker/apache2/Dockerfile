FROM ubuntu
MAINTAINER RinKeigun <huiqun.lin@gmail.com>
RUN apt-get update && apt-get -y install apache2 php
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_PID_FILE /run/apache2/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2

ADD ./htdocs /var/www

EXPOSE  80

#apachectl start
#ENTRYPOINT /usr/sbin/apache2ctl start
#CMD /usr/sbin/apache2ctl start
#CMD /usr/sbin/apache2 -D FOREGROUND 
#CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]
CMD []
ENTRYPOINT ["apachectl", "-DFOREGROUND"]

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
