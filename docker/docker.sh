#!/bin/bash

xhost +
#docker start debian
#docker exec -it debian /bin/bash
docker run -it -u myuser:dev dev:1.2 /bin/bash
