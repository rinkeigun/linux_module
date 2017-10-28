FROM ubuntu
MAINTAINER RinKeigun <huiqun.lin@gmail.com>
RUN apt-get update && apt-get -y install gdb gcc g++ make \
	global doxygen \
	vim git \
	language-pack-ja-base language-pack-ja ibus-mozc \
	eclipse x11-apps \
	python3 python3-pip python3-tk python3-bs4 \
	tesseract-ocr-all python3-pil \
	python3-pyocr \
	python3-numpy python-opencv libopencv-dev \
	gpicview smplayer
RUN pip3 install requests matplotlib seaborn xlrd xlwr xlutils
RUN mkdir -p /home/myuser && \
	groupadd -g 1000 dev && \
	useradd -g dev -G sudo -s /bin/bash myuser && \
	echo 'myuser:myuser' | chpasswd && \
	mkdir /home/myuser/.eclipse
	#useradd -g dev -G sudo -s /bin/bash myuser && \
#RUN echo "¥nsu - myuser" >> /root/.bashrc
#docker run -it -u myuser:dev -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v /home/rin/tmp/docker_p:/home/myuser python_rin /bin/bash
#RUN export uid=1000 gid=1000 && \
#	mkdir -p /home/dev && \
#	echo "dev:x:${uid}:${gid}:Developer,,,:/home/dev:/bin/bash" >> /etc/passwd && \
#	echo "dev:x:${uid}:" >> /etc/group && \
#	echo "dev ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/dev && \
#	chmod 0440 /etc/sudoers.d/dev && \
#	chown ${uid}:${gid} -R /home/dev
USER dev
ENV HOME /home/myuser
ENV LANG ja_JP.UTF-8
ENV LANGUAGE "ja_JP:ja"

#docker build -t imagename .
#docker run -d -p 80:80 test apache2ctl start
#docker run -it -v /home/rin/tmp/docker_p:/docker_p ubuntu
#docker Dockerfile commands
#FROM
#RUN
#CMD
#LABEL
#MAINTAINERt
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
