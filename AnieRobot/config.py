#Copyright (C) 2022 Bgt Software @Bikashhalder @Adityahalder , Inc.[ https://t.me/BikashHalder https://t.me/Adityahalder ]
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = ""
    OWNER_ID = "1439222689"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "BikashHalder"
    TOKEN = '5430784378:AAFAZv9ARe1UdbljTWKlAhCuP9pvD0zFO0E'

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://pwbjkedt:yHtCdpZsk8IzHvS3nt3MRXWtnC9bid0m@satao.db.elephantsql.com/pwbjkedt'  # needed for any database modules
    MESSAGE_DUMP = '' # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation']
    WEBHOOK = False
    DONATION_LINK = ''
    URL = ""

    # OPTIONAL
    SUDO_USERS = [0]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = [0]  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = [0]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    MAPS_API = ''
    CERT_PATH = None
    PORT = 5432
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_ANTISPAM = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = ''  # banhammer marie sticker
    STRICT_GBAN = True
    STRICT_GMUTE = True
    CUSTOM_CMD = True  # Allow ! commands as well as /
    API_OPENWEATHER = '' # OpenWeather API

    # MEMES
    DEEPFRY_TOKEN = None

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
