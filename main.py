import telegram, logging
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram.error import (TelegramError, Unauthorized, BadRequest,
                            TimedOut, ChatMigrated, NetworkError)

from src.others.custom_filters import Private, Public
from src.others.utilities import loadHandlers
from src.private_functions import *
from src.public_functions import *

#*---------------*#
#*  BOT CONFIGS  *#
#*---------------*#
TOKEN = '1491725369:AAHSTPjwt1RjB6xLjAmCrp_5lMEbwUQ05ww'

# Logging functions
logging.basicConfig(
        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level = logging.INFO)

def main():
  bot = telegram.Bot(TOKEN) # TODO: Questa variabile viene chiamata una sola volta per una funzione serve veramente o è solo per log?
  updater = Updater(TOKEN, use_context=True)
  dispatcher = updater.dispatcher
  
  print(bot.get_me()) # Who am i?

  #*---------------------------*#
  #*  ADDING COMMANDS HANDLER  *#
  #*---------------------------*#
  # General handlers
  general_handlers = [
    CommandHandler('start', start),                                          # /start
    CallbackQueryHandler(button_handler)
  ]
  #  Private heandlers
  private_handlers = [
    CommandHandler('mostrami', show, filters=(Private)),                     # /show
    CommandHandler('nick', nick, filters=(Private)),                         # /nick
    CommandHandler('livello', level, filters=(Private)),                     # /livello
    CommandHandler('codice', code, filters=(Private)),                       # /codice
    CommandHandler(['help','aiuto'], help, filters=(Private)),               # /aiuto or /help
    CommandHandler('registrami', register, filters=(Private)),               # /registrami,
    CommandHandler('aggiorna', update, filters=(Private)),                   # /aggiorna
    MessageHandler(Filters.command & Private, unknown),                      # All commands not recognized
    MessageHandler(Filters.text & ~Filters.command & Private, non_command),  # All text without commands
  ]

  # Public heandlers
  public_handlers = [
    CommandHandler('raid', raid, filters=(Public)),                          # /raid
    CommandHandler('segnala_raid', warn, filters=(Public)),                  #/segnala_raid
    MessageHandler(Filters.status_update.new_chat_members, welcome),         # Welcome message for new users
  ]

  #*---------------------------------*#
  #*  ADDING HANDLERS TO DISPATCHER  *#
  #*---------------------------------*#
  # Load general handlers
  loadHandlers(dispatcher, general_handlers)
  
  # Load private handlers
  loadHandlers(dispatcher, private_handlers)
  
  # Load public handlers
  loadHandlers(dispatcher, public_handlers)

  # Error handlers
  dispatcher.add_error_handler(error_callback)

  # Starting bot
  updater.start_polling()
  updater.idle()

def error_callback(update, context):
  # TODO: Servenono veramente così tanti except per fare la stessa cosa? :sweat_smile:
  try:
      raise context.error
  except Unauthorized as e:
      # Remove update.message.chat_id from conversation list
      print(e)
  except BadRequest as e:
      # Handle malformed requests - read more below!
      print(e)
  except TimedOut as e:
      # Handle slow connection problems
      print(e)
  except NetworkError as e:
      # Handle other connection problems
      print(e)
  except ChatMigrated as e:
      # The chat_id of a group has changed, use e.new_chat_id instead
      print(e)
  except TelegramError as e:
      # Handle all other telegram related errors
      print(e)

if __name__ == "__main__":
  main()