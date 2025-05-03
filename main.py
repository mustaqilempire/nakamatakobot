import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("Selamat datang ke Nakama Tako Bot! 🐙")

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    print("Bot started ✅")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()