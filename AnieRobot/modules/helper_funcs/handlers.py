#Copyright-2022 // Bgt Robot Updated by @BikashHalder
#Copyright (C) 2022 Bgt Software @BikashHalder @AdityaHalder , Inc.[ https://t.me/Bikashhalder https://t.me/Adityahalder ]


import telegram.ext as tg
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Filters
from BgtRobot.modules.sql.antispam_sql import is_user_gbanned
import BgtRobot.modules.sql.blacklistusers_sql as sql
try:
    from BgtRobot import CUSTOM_CMD
except:
    CUSTOM_CMD = False

if CUSTOM_CMD:
    CMD_STARTERS = CUSTOM_CMD
else:
    CMD_STARTERS = ('!', '/')


class CustomCommandHandler(tg.CommandHandler):
    def __init__(self, command, callback, **kwargs):
        if "admin_ok" in kwargs:
            del kwargs["admin_ok"]
        super().__init__(command, callback, **kwargs)

    def check_update(self, update):
        if isinstance(update, Update) and update.effective_message:
            message = update.effective_message
            
            try: 
               user_id = update.effective_user.id
            except:
               user_id = None 
            if user_id:
                if is_user_gbanned(user_id):
                      return
            if user_id:
                if sql.is_user_blacklisted(update.effective_user.id):
                      return False

            if message.text and len(message.text) > 1:
                fst_word = message.text.split(None, 1)[0]
                if len(fst_word) > 1 and any(fst_word.startswith(start) for start in ('/', '!')):
                    args = message.text.split()[1:]
                    command = fst_word[1:].split('@')
                    command.append(message.bot.username)  # in case the command was sent without a username

                    if not (command[0].lower() in self.command
                            and command[1].lower() == message.bot.username.lower()):
                        return None

                    filter_result = self.filters(update)
                    if filter_result:
                        return args, filter_result
                    else:
                        return False
