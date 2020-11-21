import telegram
import logging
from telegram.ext import Updater
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, ChatMigrated, NetworkError)
                    
def main():
    TOKEN = '1491725369:AAHSTPjwt1RjB6xLjAmCrp_5lMEbwUQ05ww'
    bot = telegram.Bot(TOKEN)
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
    dispatcher.add_error_handler(error_callback) 
    print(bot.get_me())

def error_callback(update, context):
    try:
        raise context.error
    except Unauthorized:
        # remove update.message.chat_id from conversation list
        print(e)
    except BadRequest:
        # handle malformed requests - read more below!
        print(e)
    except TimedOut:
        # handle slow connection problems
        print(e)
    except NetworkError:
        # handle other connection problems
        print(e)
    except ChatMigrated as e:
        # the chat_id of a group has changed, use e.new_chat_id instead
        print(e)
    except TelegramError:
        # handle all other telegram related errors
        print(e)

if __name__ == "__main__":
    main()