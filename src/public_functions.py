from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import timedelta
from src.queries import *
from src.exceptions import *
from src.languages import *
from src.others.utilities import *
import json

# TODO: user friendcode e user nick
# create a raid (/raid <pokémon> <time>)
def raid(update, context):
    args = context.args
    if len(args) >= 2:
        try:
            buttons_list = [
                [InlineKeyboardButton("🚶🏻‍♂ Io ci sono!", callback_data='join'),InlineKeyboardButton("📡 Invitami", callback_data='remote')],
                [InlineKeyboardButton("🔔 Ping", callback_data='ping'),InlineKeyboardButton("💔 Passo", callback_data='skip')]
            ]
            reply = InlineKeyboardMarkup(buttons_list)
            pokemon, time = args[0].upper(), args[1]
            username = get_username(update)
            user_id = get_user_id(update)
            # friendcode = getUserFriendCode(user_id)
            friendcode = "0000 0000 0000"
            # nick = getUserNick()
            nick = "Telepig34"
            level = 31
            notes = ' '.join(args[2:])
            if username == None: raise NoUsernameException()
            
            text = parse_text("RAID_TEXT", (pokemon, time, notes, username, nick, level, friendcode))
            context.bot.send_message(chat_id = update.effective_chat.id, text=text, reply_markup=reply)
        except NoUsernameException:
            context.bot.send_message(chat_id = update.effective_chat.id, text="❌ Per creare un raid devi possedere un username!")
    else:
        context.bot.send_message(chat_id = update.effective_chat.id, text="Crea un raid digitando \"/raid pokémon orario note(opzionali)\"")

# warns admins of an invalid raid (/segnala_raid)
def warn(update, context):
    # SELECT DI STAFF
    staff = {
        "dilan": "367369885",
        "giada": "857540347"
    }
    for user_id in staff.values():
        message_date = update.message.date + timedelta(hours=1)
        message_date = message_date.strftime("%d/%m/%Y %H:%M")

        message_from_id = get_user_id(update)
        message_from_username = get_username(update)
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

