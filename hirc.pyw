import os
import sys
import time
import threading
import irc_bot_noblock
from datetime import datetime

# change it to your own
# get your oauth here: https://twitchapps.com/tmi/
nickname = ''
oauth = 'oauth:'

if(len(sys.argv) != 3):
    print (__file__ + ' chat_channel message')
    exit()

chat_channel = sys.argv[1].lower().lstrip().rstrip()
chat_server = ['irc.chat.twitch.tv', 6667]

bot = irc_bot_noblock.irc_bot(nickname, oauth, chat_channel, chat_server[0], chat_server[1], timeout=300)
bot.connect()
bot.send_message(sys.argv[2])