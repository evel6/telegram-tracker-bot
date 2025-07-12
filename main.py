import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = "https://yourapp.onrender.com"  # عدل هذا لاحقاً برابط Render الخاص بك

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    url = f"{BASE_URL}/track?id={user_id}"
    button = InlineKeyboardButton("🔍 افتح رابط التتبع", url=url)
    reply_markup = InlineKeyboardMarkup([[button]])
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="👁️‍🗨️ رابط التتبع الخاص بك:",
                             reply_markup=reply_markup)

def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
