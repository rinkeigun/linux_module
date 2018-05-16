# wechat working hours
# create table user_manage_t ( id text );
# create table working_hours_manage_t ( id text, d_str text, t_str text, flg text);

# 导入模块
from wxpy import *
import sqlite3
import threading
import os
import time
from datetime import datetime, timedelta


class weixin(threading.Thread):

    def __init__(self, mypuid):
        super(weixin, self).__init__()
        self.mypuid = mypuid

    def run(self):
        pngpath = self.mypuid+'.png'
        pklpath = self.mypuid+'.pkl'
        print( "bot : " + pklpath )
        
        # QRコード表示、ログイン待ち
        bot = Bot(cache_path=False, console_qr=True, qr_path=pngpath)
        bot.enable_puid(pklpath)
        
        # ユーザー情報の取得
        user1 = bot.self
        print( type(user1) )
        print( user1 )
        print( "1. alias      : "+user1.alias )
        print( "1. nick_name  : "+user1.nick_name )
        print( "1. user_name  : "+user1.user_name )
        print( "1. name       : "+user1.name )
        print( "1. puid       : "+user1.puid )
        
        # DB
        db = 'workinghours.db3'
        usermanaget = 'user_manage_t'
        whmanaget = 'working_hours_manage_t'
        connector = sqlite3.connect(db)
        
        # DBからユーザー情報の取得
        sql = "select id from %s where id = '%s'" % ( usermanaget, user1.name )
        cnt = len(connector.execute( sql ).fetchall())
        if cnt == 0:
            user1.send(u'未登录用户，请与群主联系')
            w = weixin(self.mypuid)
            w.start()
        else:
            first_time = datetime.now()
            d_str = first_time.strftime("%Y/%m/%d")
            sql = "select id, d_str from %s where id = '%s' and d_str = '%s'" % ( whmanaget, user1.name, d_str )
            #cnt = len(connector.execute( sql ).fetchone())
            cnt = connector.execute( sql ).fetchone()
            
            if cnt is not None:
                t_str = first_time.strftime("%H:%M:%S")
                sql = "insert into %s values( '%s', '%s', '%s', '%s' )" % ( whmanaget, user1.name, d_str, t_str, '0' )
                connector.execute( sql )
                connector.commit()
                user1.send(u'添加登录')
                w = weixin(user1.puid)
                w.start()
            else:
                newlogintimer = datetime.now()+ timedelta(seconds=15)

                # timer設定
                bot = Bot(cache_path=False, console_qr=True, qr_path=pngpath)
                bot.enable_puid(pklpath)
                user2 = bot.self
                print( "1. alias       : "+user1.alias )
                print( "1. nick_name   : "+user1.nick_name )
                print( "1. user_name   : "+user1.user_name )
                print( "1. name        : "+user1.name )
                print( "1. puid        : "+user1.puid )
                print( "1. city        : "+user1.city )
                print( "1. province    : "+user1.province )
                print( "1. remark_name : "+user1.remark_name )
                print( "1. sex         : "+str(user1.sex) )
                print( "1. signature   : "+user1.signature )
                if user1.uin is not None:print("uin       : "+str(user1.uin))
                if user1.wxid is not None:print("wxid      : "+str(user1.wxid))
                print( "2. alias       : "+user2.alias )
                print( "2. nick_name   : "+user2.nick_name )
                print( "2. user_name   : "+user1.user_name )
                print( "2. name        : "+user2.name )
                print( "2. puid        : "+user2.puid )
                if user1.name != user2.name:
                    user2.send(u'请重新登录')
                else:
                    first_time = datetime.now()
                    d_str = first_time.strftime("%Y/%m/%d")
                    t_str = first_time.strftime("%H:%M:%S")
                    sql = "insert into %s values( '%s', '%s', '%s', '%s' )" % ( whmanaget, user2.name, d_str, t_str, '1' )
                    print( sql )
                    connector.execute( sql )
                    connector.commit()
                    user2.send(u'新登录')
                w = weixin(user2.puid)
                w.start()
                
                '''
                last_time = datetime.now()
                #d_str = last_time.strftime("%Y/%m/%d %H:%M:%S")
                #delta = last_time - first_time
                #print (delta.total_seconds())
                @bot.register(except_self=False, enabled=True)
                def reply_my_friend(msg):
                    print(msg)
                    try:
                        print("alias     : "+msg.sender.alias)
                        print("nick_name : "+msg.sender.nick_name)
                        print("user_name : "+msg.sender.user_name)
                        print("name      : "+msg.sender.name)
                        print("puid      : "+msg.sender.puid)
                        #print("uin       : "+msg.sender.uin)
                        #print("wxid      : "+msg.sender.wxid)
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
                                w = weixin(msg.sender.puid)
                                w.start()
                                imgpath = msg.sender.puid+'.png'
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
                '''
        print (u'启动了')
        bot.join()
        
if __name__ == '__main__':
    user_name = '086a9197'
    w = weixin(user_name)
    w.start()
