# host : 
# mkdir /some/content
# vi /some/content/index.html
# docker build -t imagename .
# docker run --name some-nginx -p 80:80 -v /some/content:/usr/share/nginx/html:ro -d nginx
# curl http://0.0.0.0:80/index.html
# other command:
#    docker stop `docker ps -a -q`
#    docker rm `docker ps -a -q`
# 
FROM ubuntu:14.04

MAINTAINER K.Rin <huiqun.lin@gmail.com>

RUN apt-get update && \
    apt-get install -y -q nginx && \
    rm -Rf /etc/nginx/sites-enabled/default && \
    rm -rf /var/lib/apt/lists/*

VOLUME ["/etc/nginx","/var/log/nginx"]

EXPOSE 443
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]



