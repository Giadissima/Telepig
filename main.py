import telegram
import logging
import json
from src.dm_functions import *
from src.groups_functions import *
from telegram.ext import Updater,  CommandHandler, CallbackQueryHandler
from src.custom_filters import Private, Public
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

    '''  ADDING COMMANDS HANDLER  '''
    # /start
    start_handler = CommandHandler('start', start)
    '''   private's commands   '''
    # /aiuto or /help
    help_handler = CommandHandler(['help','aiuto'], help, filters=(Private))
    dev_handler = CommandHandler(['test','dev'], devTestingFunction)
    # all commands not recognized in dm
    unknown_handler = MessageHandler(Filters.command & Private, unknown)
    # all text without commands
    non_command_handler = MessageHandler(Filters.text & ~Filters.command, non_command) 
    # adding multiple dispatcher
    dispatcher.add_handler(CallbackQueryHandler(button_pressed))
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(dev_handler)

    dispatcher.add_handler(non_command_handler)
    dispatcher.add_handler(unknown_handler)

    # add error handler
    dispatcher.add_error_handler(error_callback) 
    # starting to listen
    updater.start_polling()
    updater.idle()
    # who am i?
    print(bot.get_me())

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