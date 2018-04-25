# 导入模块
from wxpy import *
import sqlite3
# 初始化机器人，扫码登陆
bot = Bot(cache_path=True, console_qr=True)

#db = ':memory:'
#db = 'test.db3'
#tablename = 'wechat_control_t'
#connector = sqlite3.connect(db)
#createtable = "create table IF NOT EXISTS %s (flg INTEGER)" % tablename
#connector.execute( createtable )

#sql = "insert into %s values( '%s')" % (tablename, 1)
#print ( sql )
#connector.execute( sql )
#connector.close()



my_friend_list = bot.friends()

@bot.register([friend for friend in my_friend_list], except_self=False, enabled=True)
def reply_my_friend(msg):
	#db = ':memory:'
	db = 'test.db3'
	tablename = 'wechat_control_t'
	connector = sqlite3.connect(db)
	if msg.sender == msg.receiver:
		if msg.text == 'c1 on':
			flg = 1
		elif msg.text == 'c1 off':
			flg = 0
		else:
			sql = "select flg from %s" % ( tablename )
			flg = connector.execute( sql ).fetchone()[0]
		sql = "update %s set flg = %d " % ( tablename, flg )
		connector.execute( sql )
		connector.commit()
	else:
		sql = "select flg from %s" % ( tablename )
		print( connector.execute( sql ).fetchone()[0] )
		if connector.execute( sql ).fetchone()[0] == 1:
			return u'睡觉时间，醒后回复'

#@bot.register([friend for friend in my_friend_list], except_self=False)
#@bot.register([friend for friend in my_friend_list], except_self=False)
#def reply_control(msg):
#	print( msg.text == 'c1 on')
#
#	if msg.sender == msg.receiver:
#		if msg.text == 'c1 on':
#			bot.registered.enable(reply_my_friend)
#		elif msg.text == 'c1 off':
#			bot.registered.disable(reply_my_friend)
#	else:
#		pass

print (u'启动了')
bot.join()