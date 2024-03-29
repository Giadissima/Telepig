import telegram
import logging
from telegram.ext import Updater,  CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
from src.private_functions import *
from src.public_functions import *
from src.others.custom_filters import Private, Public
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
    
    # who am i?
    print(bot.get_me(), "\n\n")

    '''  ADDING COMMANDS HANDLER  '''
    start_handler = CommandHandler('start', start) # /start
    '''   private commands   '''
    show_handler = CommandHandler('mostrami', show, filters=(Private)) # /show
    nick_handler = CommandHandler('nick', nick, filters=(Private)) # /nick
    level_handler = CommandHandler('livello', level, filters=(Private)) # /livello
    code_handler = CommandHandler('codice', code, filters=(Private)) # /codice
    help_handler = CommandHandler(['help','aiuto'], help, filters=(Private)) # /aiuto or /help
    register_handler = CommandHandler('registrami', register, filters=(Private)) # /registrami,
    update_handler = CommandHandler('aggiorna', update, filters=(Private)) # /aggiorna
    unknown_handler = MessageHandler(Filters.command & Private, unknown) # all commands not recognized in dm
    non_command_handler = MessageHandler(Filters.text & ~Filters.command & Private, non_command)  # all text without commands
    '''   public commands   '''
    raid_handler = CommandHandler('raid', raid, filters=(Public)) # /raid
    warn_handler = CommandHandler('segnala_raid', warn, filters=(Public)) #/segnala_raid

    '''  ADDING MULTIPLE DISPATCHER  '''
    '''   general commands   '''
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(CallbackQueryHandler(button_handler))
    dispatcher.add_error_handler(error_callback) # add error handler
    welcome_handler = MessageHandler(Filters.status_update.new_chat_members, welcome) # /welcome
    '''   private commands   '''
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(register_handler)
    dispatcher.add_handler(nick_handler)
    dispatcher.add_handler(level_handler)
    dispatcher.add_handler(code_handler)
    dispatcher.add_handler(show_handler)
    dispatcher.add_handler(update_handler)
    dispatcher.add_handler(non_command_handler)
    dispatcher.add_handler(unknown_handler)
    '''   public commands   '''
    dispatcher.add_handler(warn_handler)
    dispatcher.add_handler(raid_handler)
    dispatcher.add_handler(welcome_handler)

    # starting to listen
    updater.start_polling()
    updater.idle()

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