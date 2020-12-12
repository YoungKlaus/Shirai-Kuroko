# Author: Klaus
# Date: 2020/12/12 21:52

import logging
from telegram import Audio
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random
import os
#
# os.environ["http_proxy"] = "http://127.0.0.1:7890"
# os.environ["https_proxy"] = "http://127.0.0.1:7890"
# Enable logging
TOKEN = os.getenv("TOKEN")
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    # update.message.reply_text(update.message.text)

    if "黑子" in update.message.text:
        update.message.reply_text('风纪委员第3/177活动支部,白井黑子报道！')
    elif "Klaus" in update.message.text:
        update.message.reply_text('Klaus 赛高！')
    elif "吃饭" in update.message.text:
        update.message.reply_text('又想不好去哪吃饭了吗？')
    else:
        pass


def audio(update: Update, context: CallbackContext) -> None:
    previous_text = update.message.text
    chat_id = update.message.chat_id
    voice_key = 0
    voice_dic = {
        "难道": "http://drive.iklaus.design/?/voice/%E4%B8%8D%E4%BC%9A%E5%90%A7.mp3",
        "准备": "http://drive.iklaus.design/?/voice/%E4%B9%9F%E5%8F%AA%E8%83%BD%E5%87%86%E5%A4%87%E5%88%B0%E8%BF%99%E4%BA%9B%E4%BA%86.mp3",
        "简单": "http://drive.iklaus.design/?/voice/%E4%BB%80%E4%B9%88%E5%98%9B%20%E5%B0%8F%E8%8F%9C%E4%B8%80%E7%A2%9F%E5%98%9B.mp3",
        "黑子": "http://drive.iklaus.design/?/voice/%E4%BD%A0%E5%A5%BD%20%20%20%20%E6%88%91%E6%98%AF%E7%99%BD%E4%BA%95.mp3",
        "笑": "http://drive.iklaus.design/?/voice/%E5%82%BB%E7%AC%91.mp3",
        "发生": "http://drive.iklaus.design/?/voice/%E5%8F%91%E7%94%9F%E4%BB%80%E4%B9%88%E4%BA%8B%E4%BA%86.mp3",
        "怎么回事": "http://drive.iklaus.design/?/voice/%E5%93%8E.....%E5%93%8E.....mp3",
        "怎么样": "http://drive.iklaus.design/?/voice/%E5%95%8A%EF%BC%8C%E4%B8%8D%E8%BF%87....mp3",
        "御坂美琴": random.choice([
                                  "http://drive.iklaus.design/?/voice/%E5%A7%90%E5%A7%90%E5%A4%A7%E4%BA%BA%20%E5%A7%90%E5%A7%90%E5%A4%A7%E4%BA%BA.mp3",
                                  "http://drive.iklaus.design/?/voice/%E5%A7%90%E5%A7%90%E5%A4%A7%E4%BA%BA.mp3"]),
        "知道": random.choice(["http://drive.iklaus.design/?/voice/%E6%88%91%E6%98%8E%E7%99%BD%E4%BA%86.mp3",
                             "http://drive.iklaus.design/?/voice/%E6%98%8E%E7%99%BD%E4%BA%86.mp3",
                             "http://drive.iklaus.design/?/voice/%E6%98%AF...%E6%98%AF.mp3",
                             "http://drive.iklaus.design/?/voice/%E9%9D%9E%E5%B8%B8%E4%BA%86%E8%A7%A3.mp3",
                             "http://drive.iklaus.design/?/voice/%E9%BB%91%E5%AD%90%E6%88%91%E6%97%A9%E5%B0%B1%E7%9F%A5%E9%81%93%E4%BA%86.mp3"]),
        "是吗": "http://drive.iklaus.design/?/voice/%E6%98%AF...%E6%98%AF.mp3",
        "黑子是": "http://drive.iklaus.design/?/voice/%E6%88%91%E6%98%AF%E9%A3%8E%E7%BA%AA%E5%A7%94%E5%91%98.mp3",
        "又": random.choice([
                               "http://drive.iklaus.design/?/voice/%E7%9C%9F%E6%98%AF%E7%9A%84%20%EF%BC%88%E8%AF%AD%E6%B0%94%E4%B8%8D%E5%90%8C%EF%BC%89.mp3",
                               "http://drive.iklaus.design/?/voice/%E7%9C%9F%E6%98%AF%E7%9A%84.mp3"]),
        "不知道": "http://drive.iklaus.design/?/voice/%E8%A3%85%E5%82%BB%E4%B9%9F%E6%98%AF%E6%B2%A1%E7%94%A8%E7%9A%84.mp3",
        "是吧": "http://drive.iklaus.design/?/voice/%E8%AF%B4%E7%9A%84%E4%B9%9F%E6%98%AF.mp3",
        "怎么了": "http://drive.iklaus.design/?/voice/%E9%82%A3%E4%B8%AA....%E9%82%A3%E4%B8%AA....mp3",
        "确定": "http://drive.iklaus.design/?/voice/%E9%82%A3%E6%98%AF%E5%BD%93%E7%84%B6%E5%95%A6.mp3",
        "风纪委员": "http://drive.iklaus.design/?/voice/%E9%A3%8E%E7%BA%AA%E5%A7%94%E5%91%98%E7%9A%84%E5%B7%A5%E4%BD%9C%E5%8F%AF%E6%B2%A1%E9%82%A3%E4%B9%88%E8%BD%BB%E6%9D%BE%E5%93%A6.mp3"

    }
    for x in voice_dic:
        if x in previous_text:
            voice_key = x

    if voice_key != 0:
        context.bot.send_audio(chat_id=chat_id, audio=voice_dic[voice_key])


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)
    bot = updater.bot
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, audio))
    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()


