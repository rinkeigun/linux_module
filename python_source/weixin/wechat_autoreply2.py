# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot(cache_path=True, console_qr=True)

my_friend_list = bot.friends()

#@bot.register([friend for friend in my_friend_list], enabled=True)
#def reply_my_friend(msg):
#	print( "reply_my_friend")
#	if msg.sender == msg.receiver:
#		print('sender')
#	else:
#		return u'睡觉时间，醒后回复'

@bot.register([friend for friend in my_friend_list], except_self=False)
#@bot.register([friend for friend in my_friend_list], except_self=False)
def reply_control(msg):
	print( msg.text == 'c1 on')
	print(bot.registered())

	if msg.sender == msg.receiver:
		if msg.text == 'c1 on':
			bot.registered.enable(reply_my_friend)
		elif msg.text == 'c1 off':
			bot.registered.disable(reply_my_friend)
	else:
		pass
	#bot.register.enabled

print (u'启动了')
bot.join()