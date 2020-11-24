from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def raid(update, context):
    args = context.args
    if len(args) >= 2:
        buttons_list = [
            [InlineKeyboardButton("🚶🏻‍♂ Io ci sono!", callback_data='join'),InlineKeyboardButton("📡 Invitami", callback_data='remote')],
            [InlineKeyboardButton("🔔 Ping", callback_data='ping'),InlineKeyboardButton("💔 Passo", callback_data='skip')],
        ]
        reply = InlineKeyboardMarkup(buttons_list)
        context.bot.send_message(chat_id = update.effective_chat.id, text="Pokèmon: {}\nOrario: {}\nNote: {}".format(args[0], args[1], ' '.join(args[2:])), reply_markup=reply)
    else:
        context.bot.send_message(chat_id = update.effective_chat.id, text="Crea un raid digitando \"/raid pokémon orario note(opzionali)\"")

def button_handler(update, context):
    query = update.callback_query
    query.edit_message_text(text=query.data)