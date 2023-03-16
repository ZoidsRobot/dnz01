#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "10802796"
API_HASH = "191107910c6fbc576bff320d6f4e8d12"
BOT_TOKEN = "5885677035:AAFFwI52ayU947kQvCmOBnvuj03AVOy208s"
SESSION = "AQBgehDWR_RB269E8haXjj4ltNIGFS_2TJKOPErl3rmqhnnu0rf1-R7TcqLcFx4BPY6BT3FO5MhwK06Zgc54GxZb7jCWaW-gkvRRZiUoKINE3QygNxK3ZbYq7QWx4IJScvzFhgj4uYIg7uXMiqVA4vUSt0jV1zGIPNG0HHgUAAy9BXq4VBSq8i3dmsEqaeUnJbnSIatR0Zdm7i8kC7m2F0jabE51bc1paqiW2o_jDqeJqJB_71Jia2HIdC-q5ct5MC2LdSjUy9ibHYmJPlHt65KEWyaOoCe5A5exOmgnmUtVaojzlLx3XoPn2dzRhaiy35_Fl851nzUQ3WhJF-q5My92AAAAAUZCL70A"
FORCESUB = "DuniaVirtualMenfess"
AUTH = 5473710013

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
