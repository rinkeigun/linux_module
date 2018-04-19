# coding: utf-8
# pip install wechat_sender

from __future__ import unicode_literals

from wxpy import *
from wechat_sender import listen

bot = Bot('bot.pkl')

my_friend_list = bot.friends().search('黄英兰')

print( my_friend_list)


#my_friend = bot.friends().search('yinglanhuang')[0]
my_friend = my_friend_list[0]

my_friend.send('我爱你')

@bot.register(Friend)
def reply_test(msg):
    msg.reply('test')

listen(bot) # 只需改变最后一行代码