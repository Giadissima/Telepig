import re
from src.queries import *
from src.utilities import *

def start(update, context):
    """when bot receives /start"""
    message_received(update)
    sending_message(update)
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Ciao sono Telepig! 
    \nPosso aiutarti a creare dei raid. 
    \nPer favore ricorda che per utilizzarmi è necessario registrarsi. Digita /register per effettuare la registrazione.""")

def unknown(update, context):
    """when bot receives unknown commands"""
    message_received(update)
    sending_message(update)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Mi spiace, non conosco questo comando. Digita /aiuto per ulteriori informazioni.")

def non_command(update, context):
    """when bot receives invalid text"""
    message_received(update)
    sending_message(update)
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Hey! 
Ma che lingua parli? Digita \"/\" seguito da un comando per poter dialogare con me 🤪""")

def help(update, context):
    """when bot receives /help or /aiuto"""
    message_received(update)
    sending_message(update)
    text = """Comandi: 
/registrami - Usa questo comando per registrarti.
/mostrami - Mostra le tue informazioni salvate.
/aggiorna - Usa questo comando per aggiornare il tuo profilo."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def register(update, context):
    """when bot receives /register"""
    message_received(update)
    sending_message(update)
    if (is_user_into_db(get_user_id(update))):
        text = """Sembra che tu sia registrato... 💩 se vuoi vedere le tue informazioni salvate, digita /mostrami"""
    else:
        text = """Registrati usando i sottocomandi:
/nick iltuonickname
/livello iltuolivello
/codice iltuocodiceamico
ricordati che devi effettuare tutti i passaggi per completare la registrazione."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def update(update, context):
    """when bot receives /aggiorna"""
    message_received(update)
    sending_message(update)
    if not is_registered(update):
        text = """Sembra che tu non sia registrato... 💩 se vuoi registrarti digita /registrami"""
    else:
        text = """Aggiorna il tuo profilo usando i sottocomandi:
/nick iltuonickname
/livello iltuolivello
/codice iltuocodiceamico""" 
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

# when bot receives /nick
# TODO: update e insert
def nick(update, context):
    """when bot receives /nick"""
    message_received(update)
    sending_message(update)
    args = context.args
    if len(args) == 1:
        context.bot.send_message(chat_id = update.effective_chat.id, text="Il tuo nickname è stato aggiornato")
        if is_registered(update):
            # UPDATE
            pass
        else:
            # INSERT
            pass
    else:
        context.bot.send_message(chat_id = update.effective_chat.id, text="/nick iltuonickname")

# TODO: update e insert
def level(update, context):
    """   when bot receives /livello   """
    message_received(update)
    sending_message(update)
    args = context.args
    if len(args) == 1:
        try:
            args[0] = int(args[0])
            if args[0] < 9 or args[0] > 50:
                context.bot.send_message(chat_id = update.effective_chat.id, text="Il livello inserito non è in un range valido 9-50.")
            else:
                context.bot.send_message(chat_id = update.effective_chat.id, text="Il tuo livello è stato aggiornato.")
                if is_registered(update):
                    # UPDATE
                    pass
                else:
                    # INSERT
                    pass
        except ValueError:
            context.bot.send_message(chat_id = update.effective_chat.id, text="Il livello inserito non è un numero valido")
    else:
        context.bot.send_message(chat_id = update.effective_chat.id, text="/level iltuolivello")

# TODO: update e insert
def code(update, context):  
    '''   when bot receives /codice insert user's friend code into  db   '''  
    message_received(update)
    sending_message(update)
    args = context.args
    if len(args) > 0:
        if re.match('^[0-9]{12}$', ''.join(args)):
            context.bot.send_message(chat_id = update.effective_chat.id, text="Il tuo codice amico è stato aggiornato.")
            if is_registered(update):
                # UPDATE
                pass
            else:
                # INSERT
                pass
        else:
            context.bot.send_message(chat_id = update.effective_chat.id, text="Hai inserito un codice non valido.")
    else:
        context.bot.send_message(chat_id = update.effective_chat.id, text="/codice iltuocodice")

# TODO: Select from db
def show(update, context):
    '''   when bot receives /mostrami   '''
    message_received(update)
    sending_message(update)
    if is_registered(update):
        text = """Cooming Sooooooooon 🤡🕰"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Digita /registrami per registrarti")

def welcome(update, context):
    '''   when a new member enter in the group   '''
    text = """Benvenuto! Io sono Telepig, aiuto gli allenatori a organizzare i raid.
Per favore, scrivimi per effettuare la registrazione."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def message_received(update):
    '''   print on terminal the user info   '''
    print("message received by: ", update.effective_chat.id, "\n\tuser: ", update.effective_chat.username, "\n\ttext: ", update.message.text)

def sending_message(update):
    '''   print on terminal the user which you're replying   '''
    print("sending message reply to...", update.effective_chat.id, "\n\tuser:", update.effective_chat.username)
