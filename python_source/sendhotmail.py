# -*- coding: utf-8 -*-
import sys
import ssl
import smtplib

from email import encoders
#from email.MIMEText import MIMEText
#from email.Utils import formatdate
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

#hotmail
#user = 'huiqun<linhuiqun_us@hotmail.com>'
user = 'linhuiqun_us@hotmail.com'

def create_message(from_addr, to_addr, subject, body, attach_file):
    #msg = MIMEText(body)
    msg = MIMEMultipart(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()
    
    # 添付ファイルのMIMEタイプを指定する
    #mime={'type':'text', 'subtype':'comma-separated-values'}
    # bin	application/octet-stream
    # css	text/css
    # csv	text/csv
    # doc	application/msword
    # gif	image/git
    # htm	text/html
    # html	text/html
    # ico	image/x-icon
    # jpeg	image/jpeg
    # jpg	image/jpeg
    # js	application/js
    # json	application/json
    # mpeg	video/mpeg
    # pdf	application/pdf
    # ppt	application/vnd.ms-powerpoint
    # rar	application/x-rar-compressed
    # rtf	application/rtf
    # tar	application/tar
    # tif	image/tiff
    # tiff	image/tiff
    # ttf	application/x-font-ttf
    # wav	audio/x-wav
    # xls	application/vnd.ms-excel
    # zip	application/zip
    # 7z	application/x-7z-compressed
    #mime={'type':'text', 'subtype':'comma-separated-values'}
    mime={'type':'text', 'subtype':'plain'}
    attachment = MIMEBase(mime['type'],mime['subtype'])
    # 添付ファイルのデータをセットする
    file = open(attach_file['path'])
    attachment.set_payload(file.read())
    file.close()
    encoders.encode_base64(attachment)
    msg.attach(attachment)
    attachment.add_header("Content-Disposition","attachment", filename=attach_file['name'])
    return msg

def send(from_addr, to_addr, msg, passwd):
    _DEFAULT_CIPHERS = (
        'ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
        'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES:!aNULL:'
        '!eNULL:!MD5')
    # SMTPの引数を省略した場合はlocalhost:25
    s = smtplib.SMTP('smtp-mail.outlook.com', 587)
    s.set_debuglevel(True)
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.options |= ssl.OP_NO_SSLv2
    context.options |= ssl.OP_NO_SSLv3

    context.set_ciphers( _DEFAULT_CIPHERS)
    context.set_default_verify_paths()
    context.verify_mode = ssl.CERT_REQUIRED
    
    if s.starttls(context=context)[0] != 220:
        return False

    s.login(user, passwd)
    try:
        s.sendmail(from_addr, [to_addr], msg.as_string())
    finally:
        s.quit()
    s.close()

if __name__ == '__main__':
    #from_addr = 'huang@innov-soft.co.jp'
    from_addr = user 
    to_addr = 'huiqun.lin@gmail.com'
    attach_file={'name':'text.txt', 'path':'text.txt'}
    msg = create_message(from_addr, to_addr, u'日本語test subject', 'よろしくtest body', attach_file)
    passwd = sys.argv[1]
    send(from_addr, to_addr, msg, passwd)
