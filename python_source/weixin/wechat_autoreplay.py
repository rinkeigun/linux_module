# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot(cache_path=True)

friends = []
my_friend_list = bot.friends()
[print( friend) for friend in my_friend_list]
#for friend in my_friend_list:
	#print( "remark_name:" + friend.remark_name )
	#print( "signature:" + friend.signature )
	#print( "name:" + friend.name )
	#print( "nick_name:" + friend.nick_name )
	#print( "puid:" + friend.puid )
	#print( "user_name:" + friend.user_name )
	#friend_name = friend.toString().split(': ')[1]
	#print( friend_name[:len(friend_name)] )
#	@bot.register(friend.name)



my_friend = bot.friends().search('黄英兰')[0]
print(my_friend)

# 获取所有类型的消息（好友消息、群聊、公众号，不包括任何自己发送的消息）
# 并将获得的消息打印到控制台
#@bot.register()
#def print_others(msg):
#    print(msg)

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
#my_friend1 = bot.friends().search('林理恵')[0]
#@bot.register(my_friend)

#@bot.register(my_friend1)
@bot.register([friend for friend in my_friend_list])
#[@bot.register(friend) for friend in my_friend_list]
def reply_my_friend(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)

bot.join()
#embed()