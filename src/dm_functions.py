

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
