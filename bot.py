# Author: Klaus
# Date: 2020/12/15 23:59


import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random
import os
from pixivpy3 import *
import requests
import shutil

TOKEN = os.getenv("TOKEN")
PIXIV_ID = os.getenv("PIXIV_ID")
PIXIV_PW = os.getenv("PIXIV_PW")
# os.environ["http_proxy"] = "http://127.0.0.1:7890"
# os.environ["https_proxy"] = "http://127.0.0.1:7890"
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Judgement desu no ! ' + "\n" + context.bot.link)


def help_command(update, context) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def pin(update, context) -> None:
    context.bot.pin_chat_message(chat_id = update.effective_chat.id, message_id=update.message.message_id)

def echo(update, context) -> None:
    """Echo the user message."""
    #update.message.reply_text(update.message.text)
    previous_message = update.message.text
    if "黑子在" in previous_message:
        reply = random.choice(["风纪委员第3/177活动支部,白井黑子报道！", "我在", "下班时间还没到吗"])
        context.bot.send_message(chat_id = update.effective_chat.id, text = reply)
    elif "klaus" in previous_message.lower():
        reply = random.choice(["Klaus💗", ":)", "(u‿ฺu✿ฺ)", "ヽ(✿ﾟ▽ﾟ)ノ"])
        context.bot.send_message(chat_id = update.effective_chat.id, text = reply)
    elif "吃饭" in previous_message:
        reply = random.choice(["又想不好去哪吃饭了吗？", "想不好就去3", "那就7吧", "京工(>▽<)", "好久没去新了", "清真吧", "2", "国防科技园？？"])
        context.bot.send_message(chat_id = update.effective_chat.id, text = reply)
    else:
        pass

def audio(update:Update, context: CallbackContext) -> None:
    previous_text = update.message.text
    chat_id = update.message.chat_id
    voice_key = 0
    voice_dic = {
        "难道" : "http://drive.iklaus.design/?/voice/ogg/%E4%B8%8D%E4%BC%9A%E5%90%A7.ogg",
        "准备" : "http://drive.iklaus.design/?/voice/ogg/%E4%B9%9F%E5%8F%AA%E8%83%BD%E5%87%86%E5%A4%87%E5%88%B0%E8%BF%99%E4%BA%9B%E4%BA%86.ogg",
        "简单" : "http://drive.iklaus.design/?/voice/ogg/%E4%BB%80%E4%B9%88%E5%98%9B-%E5%B0%8F%E8%8F%9C%E4%B8%80%E7%A2%9F%E5%98%9B.ogg",
        "黑子" : "http://drive.iklaus.design/?/voice/ogg/%E4%BD%A0%E5%A5%BD-%E6%88%91%E6%98%AF%E7%99%BD%E4%BA%95.ogg",
        "笑" : "http://drive.iklaus.design/?/voice/ogg/%E5%82%BB%E7%AC%91.ogg",
        "发生" : "http://drive.iklaus.design/?/voice/ogg/%E5%8F%91%E7%94%9F%E4%BB%80%E4%B9%88%E4%BA%8B%E4%BA%86.ogg",
        "怎么回事" : "http://drive.iklaus.design/?/voice/ogg/%E5%93%8E.....%E5%93%8E.....ogg",
        "怎么样": "http://drive.iklaus.design/?/voice/ogg/%E5%95%8A%EF%BC%8C%E4%B8%8D%E8%BF%87....ogg",
        "御坂美琴" : random.choice(["http://drive.iklaus.design/?/voice/ogg/%E5%A7%90%E5%A7%90%E5%A4%A7%E4%BA%BA-%E5%A7%90%E5%A7%90%E5%A4%A7%E4%BA%BA.ogg" , "http://drive.iklaus.design/?/voice/ogg/%E5%A7%90%E5%A7%90%E5%A4%A7%E4%BA%BA.ogg"]),
        "知道" : random.choice(["http://drive.iklaus.design/?/voice/ogg/%E6%88%91%E6%98%8E%E7%99%BD%E4%BA%86.ogg" , "http://drive.iklaus.design/?/voice/ogg/%E6%98%8E%E7%99%BD%E4%BA%86.ogg" , "http://drive.iklaus.design/?/voice/ogg/%E6%98%AF...%E6%98%AF.ogg" , "http://drive.iklaus.design/?/voice/ogg/%E9%9D%9E%E5%B8%B8%E4%BA%86%E8%A7%A3.ogg" , "http://drive.iklaus.design/?/voice/ogg/%E9%BB%91%E5%AD%90%E6%88%91%E6%97%A9%E5%B0%B1%E7%9F%A5%E9%81%93%E4%BA%86.ogg"]),
        "是吗" : "http://drive.iklaus.design/?/voice/ogg/%E6%98%AF...%E6%98%AF.ogg",
        "黑子是" : "http://drive.iklaus.design/?/voice/ogg/%E6%88%91%E6%98%AF%E9%A3%8E%E7%BA%AA%E5%A7%94%E5%91%98.ogg",
        "又" : random.choice(["http://drive.iklaus.design/?/voice/ogg/%E7%9C%9F%E6%98%AF%E7%9A%84-%EF%BC%88%E8%AF%AD%E6%B0%94%E4%B8%8D%E5%90%8C%EF%BC%89.ogg" , "http://drive.iklaus.design/?/voice/ogg/%E7%9C%9F%E6%98%AF%E7%9A%84.ogg"]),
        "不知道" : "http://drive.iklaus.design/?/voice/ogg/%E8%A3%85%E5%82%BB%E4%B9%9F%E6%98%AF%E6%B2%A1%E7%94%A8%E7%9A%84.ogg",
        "是吧" : "http://drive.iklaus.design/?/voice/ogg/%E8%AF%B4%E7%9A%84%E4%B9%9F%E6%98%AF.ogg",
        "怎么了" : "http://drive.iklaus.design/?/voice/ogg/%E9%82%A3%E4%B8%AA....%E9%82%A3%E4%B8%AA....ogg",
        "确定" : "http://drive.iklaus.design/?/voice/ogg/%E9%82%A3%E6%98%AF%E5%BD%93%E7%84%B6%E5%95%A6.ogg",
        "风纪委员" : "http://drive.iklaus.design/?/voice/ogg/%E9%A3%8E%E7%BA%AA%E5%A7%94%E5%91%98%E7%9A%84%E5%B7%A5%E4%BD%9C%E5%8F%AF%E6%B2%A1%E9%82%A3%E4%B9%88%E8%BD%BB%E6%9D%BE%E5%93%A6.ogg"

    }
    for x in voice_dic:
        if x in previous_text:
            voice_key = x

    if voice_key !=0:
        context.bot.send_voice(chat_id=chat_id ,voice=voice_dic[voice_key])

def send_stickers(update, context):
    if "表情" in update.message.text:
        stickerid = random.choice(["CAACAgIAAxkBAAEBrTRf1gb3RVHegzT0NuY0BFckkOuCDQACG18AAuCjggfVMqGQj3vXGh4E",
                                   "CAACAgEAAxkBAAEBrTZf1gjfrreCTPp8ixVAOeQ6hS8h0AAC2gADOMBgRQrDy4jCg5MQHgQ",
                                   "CAACAgQAAxkBAAEBrThf1gjjad9o3lYTrpxC7g7MgfeWNQACqAADSVveCv5XzJshbIjeHgQ",
                                   "CAACAgQAAxkBAAEBrTpf1gjxmDSpXw-KnE5GxdAVZN1ZLAACEQEAAklb3gqaXLzlGci2QR4E",
                                   "CAACAgEAAxkBAAEBrTxf1gj7k8ckdLKwUkFxu5Wn33PypgACXwUAAmbKaAmZfxtTTPuKxx4E",
                                   "CAACAgEAAxkBAAEBrT5f1gkCbmKzf798p6CC2agT_k7vMAACtQQAAmbKaAnUIkHuZxnYrx4E",
                                   "CAACAgIAAxkBAAEBrUBf1gkIGaD_IXXBHd8jG-DeoVzuWgACVgADwRieC3y2BEd750wLHgQ",
                                   "CAACAgIAAxkBAAEBrUJf1gkNqkydjlelRgYGnhBXiEmZGgACSgUAAsEYngstNHjUhk62jx4E",
                                   "CAACAgIAAxkBAAEBrURf1gkQV56ruQfotO7flEP7Kmm2fgACFQkAAsEYngtgcepvOQjH6B4E",
                                   "CAACAgQAAxkBAAEBrUZf1gkZ96uIB-nIeCUlqgWq70PGAgACiTQAAuOnXQVHXIbU7SKaBB4E",
                                   "CAACAgUAAxkBAAEBrUhf1gkkEgenkncKAbNYkFECNP18JAACBAADI_9oGf_jpeWn4aAJHgQ",
                                   "CAACAgUAAxkBAAEBrUpf1gkmXEdhMDu8QGb4B7Vnk5stUAACAwADI_9oGQHSYQ2Od3bKHgQ",
                                   "CAACAgUAAxkBAAEBrUxf1gknrRFQHUMEmQY2OCyGPXSlHgACAgADI_9oGSDTXOW6NWpQHgQ",
                                   "CAACAgIAAxkBAAEBrU5f1gk0ZZKcHka1YHhqc_7dK1cK0QACbgADNwVFAfk7V4pgcOcgHgQ",
                                   "CAACAgIAAxkBAAEBrVBf1gk499Qyc9ttSVyVjG0ptGE0bgACC1gAAuCjggchrKCDXEtFAAEeBA",
                                   "CAACAgIAAxkBAAEBrVJf1glJvWd7B_KsP-JepE_fDWhG1QACaQEAAhAabSLT-dGKr5wzrR4E",
                                   "CAACAgIAAxkBAAEBrVRf1glNfxAh5fGIXm4_GGUrGmRrkgACUgEAAhAabSIuniyLTLFtbh4E",
                                   "CAACAgIAAxkBAAEBrVZf1glQeUVLJ1wi359b5UoydKp5hQACUwEAAhAabSLrCVU1z_fmSR4E",
                                   "CAACAgIAAxkBAAEBrVhf1glTtxa2isE7vDdtxnwBsYNGCwACcgEAAhAabSI83ep0ey4BHR4E",
                                   "CAACAgIAAxkBAAEBrVpf1glWbojhQ0NsK5YB4u8F1HiEEwACZwEAAhAabSKA4rHilXxE_R4E",
                                   "CAACAgIAAxkBAAEBrVxf1glcK7z25gPH9mDeheoKN9F8aQACqwEAAhAabSJ4vr6RzFRsxx4E",
                                   "CAACAgIAAxkBAAEBrV5f1glej1MNjXscXwIIq06x_tyOMgACqQEAAhAabSLKfpM-j_GINx4E",
                                   "CAACAgEAAxkBAAEBrWBf1glhirBQCgsGA9buoLP5zgF_egACvgMAAuJbQAXwVHZmEW3ZVB4E"])
        context.bot.send_sticker(chat_id = update.effective_chat.id, sticker=stickerid)

# def venue(update, context):
#     if "地点" in update.message.text:
#         context.bot.send_venue(chat_id = update.effective_chat.id, latitude=-90*random.random()+90*random.random(), longitude=-180*random.random()+180*random.random())
#         #context.bot.send_venue(chat_id=update.effective_chat.id,latitude=45.0,longitude=45.0, address="a",title="a")

def pixiv(update, context):
    if "pixiv" in update.message.text:
        _USERNAME = PIXIV_ID
        _PASSWORD = PIXIV_PW
        _TEST_WRITE = False
        _REQUESTS_KWARGS = {
            # 'proxies': {
            #     'https': 'http://127.0.0.1:7890',
            # }

        }
        aapi = AppPixivAPI(**_REQUESTS_KWARGS)

        aapi.login(_USERNAME, _PASSWORD)
        if "色图" in update.message.text:
            json_result = aapi.illust_ranking(mode="day_r18")
        else:
            if " " in update.message.text:
                keyword = update.message.text.split(" ")[-1]
            else:
                keyword = "白井黑子"

            json_result = aapi.search_illust(keyword, search_target='partial_match_for_tags')
        illust = random.choice(json_result.illusts)
        large_url = illust.image_urls['large']
        # context.bot.send_message(chat_id = update.effective_chat.id, text=large_url)
        # context.bot.send_photo(chat_id = update.effective_chat.id, photo=large_url)

        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            'Referer': 'https://app-api.pixiv.net/'
        }
        get_data = requests.get(url=large_url, headers=headers).content
        data_name = illust.title + "." + large_url.split(".")[-1]
        data_path = "./pixiv/" + data_name
        if not os.path.exists("./pixiv"):
            os.mkdir("./pixiv")
        with open(data_path, "wb", ) as fp:
            fp.write(get_data)
        # context.bot.send_document(chat_id=update.effective_chat.id, document=open(data_path,"rb"))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(data_path,"rb"))

def delete_pixiv(update, context):
    if "黑子删除pixiv文件夹" in update.message.text:
        shutil.rmtree('./pixiv')
        os.mkdir('./pixiv')
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(os.listdir(os.getcwd())))

def message(update, context):
    echo(update,context)
    audio(update,context)
    send_stickers(update,context)
    # venue(update,context)
    pixiv(update, context)
    delete_pixiv(update, context)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("pin_message", pin))
    # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command,audio))
    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
