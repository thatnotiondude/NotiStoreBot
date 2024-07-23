import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from gumroad_api import search_templates
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Enter a keyword to search for Notion templates.')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Enter a keyword to search for Notion templates.')

def search(update: Update, context: CallbackContext) -> None:
    keyword = update.message.text
    results = search_templates(keyword)
    if results:
        response = "Here are the templates that match your search:\n"
        for result in results:
            response += f"- [{result['name']}]({result['short_url']})\n"
    else:
        response = "No templates found matching your search."
    update.message.reply_text(response, parse_mode='Markdown')

def main() -> None:
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, search))\
    

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
