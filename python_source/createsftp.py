# -*- coding: utf-8 -*-
 
import sys
import paramiko
 
HOST = '192.168.2.13'
USER = 'rin'
PSWD = sys.argv[1] 
 
LOCAL_PATH  = r"test.txt"
#REMOTE_PATH = "/path/to/test.txt"
REMOTE_PATH = "test.txt"
 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username=USER, password=PSWD)
 
sftp = ssh.open_sftp()
sftp.put(LOCAL_PATH, REMOTE_PATH)
sftp.get(REMOTE_PATH, LOCAL_PATH)
sftp.close()
 
ssh.close()
