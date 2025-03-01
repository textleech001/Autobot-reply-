from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '23680771'

def start(update, context):
    context.bot.send_message(chat_id=(link unavailable), text='Welcome!', reply_markup=main_menu())

def main_menu():
    keyboard = [
        [InlineKeyboardButton('Menu 1', callback_data='menu_1')],
        [InlineKeyboardButton('Menu 2', callback_data='menu_2')],
    ]
    return InlineKeyboardMarkup(keyboard)

def menu_1(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='Menu 1 selected', reply_markup=submenu_1())

def submenu_1():
    keyboard = [
        [InlineKeyboardButton('Submenu 1-1', callback_data='submenu_1_1')],
        [InlineKeyboardButton('Submenu 1-2', callback_data='submenu_1_2')],
    ]
    return InlineKeyboardMarkup(keyboard)

def submenu_1_1(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='Submenu 1-1 selected')

def submenu_1_2(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='Submenu 1-2 selected')

def echo(update, context):
    context.bot.send_message(chat_id=(link unavailable), text=update.message.text)

def automatic_reply(update, context):
    if update.message.text.lower() == 'hello':
        context.bot.send_message(chat_id=(link unavailable), text='Hi! How are you?')
    elif update.message.text.lower() == 'how are you':
        context.bot.send_message(chat_id=(link unavailable), text='I am good, thanks!')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.text, automatic_reply))
    dp.add_handler(CallbackQueryHandler(menu_1, pattern='^menu_1$'))
    dp.add_handler(CallbackQueryHandler(submenu_1_1, pattern='^submenu_1_1$'))
    dp.add_handler(CallbackQueryHandler(submenu_1_2, pattern='^submenu_1_2$'))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
