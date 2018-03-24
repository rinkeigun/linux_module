#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import sys
import os
from time import time
import datetime

# CV_FOURCC('D','I','B',' ')    = 無圧縮
# CV_FOURCC('P','I','M','1')    = MPEG-1 codec
# CV_FOURCC('M','J','P','G')    = motion-jpeg codec (does not work well)
# CV_FOURCC('M', 'P', '4', '2') = MPEG-4.2 codec
# CV_FOURCC('D', 'I', 'V', '3') = MPEG-4.3 codec
# CV_FOURCC('D', 'I', 'V', 'X') = MPEG-4 codec
# CV_FOURCC('U', '2', '6', '3') = H263 codec
# CV_FOURCC('I', '2', '6', '3') = H263I codec
# CV_FOURCC('F', 'L', 'V', '1') = FLV1 codec

#時間を取得
#d=datetime.datetime.now().isoformat()
d=datetime.datetime.now().isoformat()
filerename=str(d)+'.avi'

cameraCapture = cv2.VideoCapture(0)
fps = 30
#size = (int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
#        int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
#videoWriter = cv2.VideoWriter('output.avi', cv2.cv.CV_FOURCC('D', 'I', 'V', 'X'), fps, size)
size = (int(cameraCapture.get(3)),
        int(cameraCapture.get(4)))
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
videoWriter = cv2.VideoWriter('output.avi', fourcc, fps, size)


start=time()
while (cameraCapture.isOpened()):
	ret, frame = cameraCapture.read()
	
	if ret == True:

		# 画面表示
		cv2.imshow('frame', frame)
 
		# 圧縮
		frame = cv2.resize(frame, (640, 480))
 
		# 書き込み
		videoWriter.write(frame)
			
		# キー待ち
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

		end=time()
		if end-start >= 100:
			break
	else:
		break
os.rename('output.avi','%s'%(filerename))

# 後処理
cameraCapture.release()
videoWriter.release()
cv2.destroyAllWindows()
