import requests
import json
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater
import os
import config


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Szia")


def anyad(update, context):
    text = update.message.text
    if text.lower() == "anyad":
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="tied geci")

    elif text.lower() == "open the pod bay doors please hal":
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="I’m sorry Dave, I’m afraid I can’t do that.")


if __name__ == '__main__':
    updater = Updater(token=config.TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, anyad))
    updater.start_polling()
    updater.idle()
