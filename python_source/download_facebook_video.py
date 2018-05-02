import urllib.request
import sys

dwn_link = sys.argv[1]

file_name = 'trial_video.mp4' 
rsp = urllib.request.urlopen(dwn_link)
with open(file_name,'wb') as f:
    f.write(rsp.read())