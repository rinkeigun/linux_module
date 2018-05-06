# wechat smart home

# 导入模块
from wxpy import *
import sqlite3
import threading
import os
import time

class weixin(threading.Thread):

    def __init__(self, username):
        super(weixin, self).__init__()
        # 初始化机器人，扫码登陆
        #bot = Bot(cache_path=True, console_qr=True)
        #username = username.replace('@', '')
        self.path = username+'.png'

    def run(self):
        print( "bot : " + self.path )
        bot = Bot(cache_path=False, qr_path=self.path)
        print("bot ")

        @bot.register(except_self=False, enabled=True)
        def reply_my_friend(msg):
            try:
                print("alias     : "+msg.sender.alias)
                print("nick_name : "+msg.sender.nick_name)
                print("user_name : "+msg.sender.user_name)
                print("name      : "+msg.sender.name)
                #print("wxid      : "+msg.sender.wxid)
                #print("puid      : "+msg.sender.puid)
                #print("uin       : "+msg.sender.uin)
                db = 'test.db3'
                tablename = 'wechat_control_t'
                connector = sqlite3.connect(db)
                if msg.sender == msg.receiver:
                    str_lower = msg.text.lower()
                    if str_lower == 'h':
                        str = 'h   : help\n'
                        str += 'h s : status\n'
                        str += 'c on/off target : control target'
                        return str
                    elif str_lower == 'h s':
                        sql = "select flg from %s" % ( tablename )
                        flg = connector.execute( sql ).fetchone()[0]
                        if flg == 1:
                            return 'On'
                        else:
                            return 'Off'
                    elif 'c on' in str_lower:
                        sql = "update %s set flg = %d " % ( tablename, 1 )
                        connector.execute( sql )
                        connector.commit()
                    elif 'c off' in str_lower:
                        sql = "update %s set flg = %d " % ( tablename, 0 )
                        connector.execute( sql )
                        connector.commit()
                else:
                    str_lower = msg.text.lower()
                    if str_lower == 'r':
                        w = weixin(msg.sender.user_name)
                        w.start()
                        imgpath = msg.sender.user_name+'.png'
                        print(imgpath)
                        for cnt in range(10):
                            time.sleep( 3 )
                            if os.path.exists(imgpath):
                                msg.reply_image( imgpath )
                                break
                    elif str_lower == 'h':
                        str = 'r   : サビース申請\n'
                        return str
            except Excption as e:
                print('test start')
                print(e.args)

        print (u'启动了')
        bot.join()
        
if __name__ == '__main__':
    user_name = '@52039c68abb43f972e683a2a6f5a0003eff3f6f40592ef4dd9027f8fa0c99370'
    w = weixin(user_name)
    w.start()
