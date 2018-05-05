#pip install qrcode
#pip install pyzbar

from pyzbar.pyzbar import decode
from PIL import Image

import qrcode #qrcodeを起動
import os


# qrcode の生成
img = qrcode.make('hoge') #''内の文字をQRコードに変換
img.show() #生成したQRコードを表示
img.save('qr_img.png') #QRコードに名前をつけて保存


# QRコード(QRcode.png)の指定
image = 'weixin\\test.png'
# QRコードの読取り
data = decode(Image.open(image))
# コード内容テキストファイル(output.txt)に出力
f = open('output.txt','a')
f.write(data[0][0].decode('utf-8', 'ignore'))
f.close()

