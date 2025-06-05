
import os
import time
from telegram import Bot
from telegram.ext import CommandHandler, Updater

TOKEN = os.getenv("BOT_TOKEN", "7479003161:AAEnr-NQ-oYZ1_hc2AbTgZGzAanQmFNCoIg")
CHANNEL_ID = os.getenv("CHANNEL_ID", "@Fuck_MxATiN")

def spam(update, context):
    for i in range(258):
        context.bot.send_message(chat_id=CHANNEL_ID, text='@MxATiN')
        time.sleep(0.5)

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('spam', spam))

updater.start_polling()
updater.idle()
