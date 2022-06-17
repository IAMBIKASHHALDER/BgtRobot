#Copyright (C) 2022 Bgt Software @BikashHalder @AdityaHalder , Inc.[ https://t.me/BikashHalder https://t.me/Adityahalder ]

from telegram import ChatAction
import html
import urllib.request
import re
import json
from typing import Optional, List
import time
import urllib
from urllib.request import urlopen, urlretrieve
from urllib.parse import quote_plus, urlencode
import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from BgtRobot import dispatcher
from BgtRobot.__main__ import STATS, USER_INFO
from BgtRobot.modules.disable import DisableAbleCommandHandler
import wikipedia

def wiki(update, context):
    bot = context.bot
    args = context.args
    reply = " ".join(args)
    summary = '{} <a href="{}">more</a>'
    update.message.reply_text(summary.format(wikipedia.summary(reply, sentences=3), wikipedia.page(reply).url))
		
WIKI_HANDLER = DisableAbleCommandHandler("wiki", wiki, pass_args=True)
dispatcher.add_handler(WIKI_HANDLER)
