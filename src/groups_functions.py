from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import timedelta
import json

#
# create a raid (/raid <pokémon> <time>)
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

# warns admins of an invalid raid (/segnala_raid)
def warn(update, context):
    # SELECT DI STAFF
    staff = {
        "dilan": "367369885",
        "giada":"857540347"
    }
    for user_id in staff.values():
        message_date = update.message.date + timedelta(hours=1)
        message_date = message_date.strftime("%d/%m/%Y %H:%M")

        message_from_id = update.message.from_user['id']
        message_from_username = update.message.from_user['username']
        group_name = update.message.chat.title
        context.bot.send_message(chat_id = user_id, text="""E' stato segnalato un utente in data {},
da parte di {},
username: {},
gruppo: {}""".format(message_date, message_from_id, message_from_username, group_name))
        # TODO: Controlliamo se è un raid vero tramite l'id del messaggio
        if update.message.reply_to_message:
            context.bot.forward_message(chat_id = user_id, from_chat_id = update.message.reply_to_message.chat.id, message_id=update.message.reply_to_message.message_id)

# when a button is pressed
def button_handler(update, context):
    query = update.callback_query
    query.edit_message_text(text=query.data)