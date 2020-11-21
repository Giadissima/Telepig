import telegram
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, ChatMigrated, NetworkError)
                    
def main():
    TOKEN = '1491725369:AAHSTPjwt1RjB6xLjAmCrp_5lMEbwUQ05ww'
    bot = telegram.Bot(TOKEN)
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(
        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level = logging.INFO)
    # add commands handlers
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler(['help','aiuto'], help)
    repeat_handler = MessageHandler(Filters.text & (~Filters.command), repeat)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(repeat_handler)
    # add error handler
    dispatcher.add_error_handler(error_callback) 
    # starting to listen
    updater.start_polling()
    # who am i?
    print(bot.get_me())

# when bot receives /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Ciao sono Telepig! 
    \nPosso aiutarti a creare dei raid. 
    \nPer favore ricorda che per utilizzarmi è necessario registrarsi. Digita /register per effettuare la registrazione.""")

# when bot receives non-command messages repeats the message
def repeat(update, context):
    message_received(update)
    sending_message(update)
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# when bot receives /help or /aiuto
def help(update, context):
    message_received(update)
    sending_message(update)
    text = """Comandi: 
    /registrati - Usa questo comando per registrarti.
    /mostra - Mostra le tue informazioni salvate.
    /aggiorna - Usa questo comando per aggiornare il tuo profilo."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

# when bot receives /register
def register(update, context):
    message_received(update)
    sending_message(update)

# print on terminal the user info
def message_received(update):
    print("message received by: ", update.effective_chat.id, "\n\tuser: ", update.effective_chat.username, "\n\ttext: ", update.message.text)
    
# print on terminal the user which you're replying
def sending_message(update):
    print("sending message reply to...", update.effective_chat.id, "\n\tuser:", update.effective_chat.username)

# when an error occourred
def error_callback(update, context):
    try:
        raise context.error
    except Unauthorized as e:
        # remove update.message.chat_id from conversation list
        print(e)
    except BadRequest as e:
        # handle malformed requests - read more below!
        print(e)
    except TimedOut as e:
        # handle slow connection problems
        print(e)
    except NetworkError as e:
        # handle other connection problems
        print(e)
    except ChatMigrated as e:
        # the chat_id of a group has changed, use e.new_chat_id instead
        print(e)
    except TelegramError as e:
        # handle all other telegram related errors
        print(e)

if __name__ == "__main__":
    main()