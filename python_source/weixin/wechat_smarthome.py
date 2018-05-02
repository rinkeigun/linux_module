# wechat smart home

# 导入模块
from wxpy import *
import sqlite3
# 初始化机器人，扫码登陆
bot = Bot(cache_path=True, console_qr=True)

# db = ':memory:'
# db = 'test.db3'
# tablename = 'wechat_control_t'
# connector = sqlite3.connect(db)
# createtable = "create table IF NOT EXISTS %s (flg INTEGER)" % tablename
# connector.execute( createtable )

# sql = "insert into %s values( '%s')" % (tablename, 1)
# print ( sql )
# connector.execute( sql )
# connector.close()

#my_friend_list = bot.friends()

#@bot.register([friend for friend in my_friend_list], except_self=False, enabled=True)
@bot.register(except_self=False, enabled=True)
def reply_my_friend(msg):
	#db = ':memory:'
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

print (u'启动了')
bot.join()