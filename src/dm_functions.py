
import re

# when bot receives /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Ciao sono Telepig! 
    \nPosso aiutarti a creare dei raid. 
    \nPer favore ricorda che per utilizzarmi è necessario registrarsi. Digita /register per effettuare la registrazione.""")

# when bot receives unknown commands
def unknown(update, context):
    message_received(update)
    sending_message(update)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Mi spiace, non conosco questo comando. Digita /aiuto per ulteriori informazioni.")

def non_command(update, context):
    message_received(update)
    sending_message(update)
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Hey! 
Ma che lingua parli? Digita \"/\" seguito da un comando per poter dialogare con me 🤪""")

# when bot receives /help or /aiuto
def help(update, context):
    print(update, context)
    message_received(update)
    sending_message(update)
    text = """Comandi: 
/registrami - Usa questo comando per registrarti.
/mostrami - Mostra le tue informazioni salvate.
/aggiorna - Usa questo comando per aggiornare il tuo profilo."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

# when bot receives /register
def register(update, context):
    message_received(update)
    sending_message(update)
    if is_registered(update):
        text = """Sembra che tu sia registrato... 💩 se vuoi vedere le tue informazioni salvate, digita /mostrami"""
    else:
        text = """Registrati usando i sottocomandi:
/nick iltuonickname
/livello iltuolivello
/codice iltuocodiceamico"""
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

# when bot receives /aggiorna
def update(update, context):
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
def nick(update, context):
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

# when bot receives /livello
def level(update, context):
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

# when bot receives /codice
def code(update, context):    
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

# check is user is into db
def is_registered(update):
    return True

# when bot receives /mostrami
def show(update, context):
    if is_registered(update):
        text = """Cooming Sooooooooon 🤡🕰"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Digita /registrami per registrarti")

# print on terminal the user info
def message_received(update):
    print("message received by: ", update.effective_chat.id, "\n\tuser: ", update.effective_chat.username, "\n\ttext: ", update.message.text)

# print on terminal the user which you're replying
def sending_message(update):
    print("sending message reply to...", update.effective_chat.id, "\n\tuser:", update.effective_chat.username)
