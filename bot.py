from telegram.ext import Filters, MessageHandler, Updater
import config


def echo(bot, update):
    update.message.reply_text(update.message.text)


if __name__ == '__main__':
    updater = Updater(token=config.TOKEN, request_kwargs={'proxy_url': config.protocol + config.ip + config.port})
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()
