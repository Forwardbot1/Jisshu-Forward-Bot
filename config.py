# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "21723836")
    API_HASH = environ.get("API_HASH", "f755ab041ac9ab14ab0c25606dd92156")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7597963888:AAFGOCPLY0r7lPrFY4EmKucazqDyitMLAB8") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7052947046').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://magandi.onrender.com/lrH_.JPG'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://forwardbot17:rvforward1@cluster0.ubuxz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002368170677'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/+oEdNLLiTXwU2YmY1") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
