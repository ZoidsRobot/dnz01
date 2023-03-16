#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "9848283"
API_HASH = "c4e36306a2c11dab87bcc8826cba7fc7"
BOT_TOKEN = "5908148910:AAFgpyHPAkcSnpyd1qMHsQ1b3TacAx1aSPg"
SESSION = "BQBEXKXvxwIGmABywr6qBsqR1TzXgwip40FSM_JLpQGhWzy5vXG2gBtQo5MaFOdWa9UG1-fPLpkl7Y1WXaY1tGAXqaZs7YIfp9XKAtBM3tFjMHbqZ5Pdj2GKMjCLx-ZH9XDvcgpL4jaM_bhX3Ticz7YdkJyqw_VvL4CpXXxH8Gmz8OuJMSW4hMPPWyUH0zSoxY3gxIdE1UdpWuE4EjO23TMvblEWAzgeR5at6CPtyG-ZlxkPAvCAJ0UeUvytyfMqILWxACkFoVSC4hrrh97bi6778O4p8oxW8ltJNFi3CpadvD2pk77Z_B_oXlCq3jp7-NzFESt6GMgIO_Wf20ZOJWOLc5MdwgA"
FORCESUB = "sedotkuy"
AUTH = 1939021250

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
