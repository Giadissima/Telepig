from telegram import InlineKeyboardButton, InlineKeyboardMarkup
def devTestingFunction(update, context):
    buttons_list = [
        InlineKeyboardButton('Button1', callback_data='Button1'),
        InlineKeyboardButton('Button2', callback_data='Button2'),
        InlineKeyboardButton('Button3', callback_data='Button3'),
        InlineKeyboardButton('Button4', callback_data='Button4')
    ]
    reply = InlineKeyboardMarkup(build_menu(buttons_list, n_cols=2))
    context.bot.send_message(chat_id = update.effective_chat.id, text="Sono con una puzzetta a programmare", reply_markup=reply)

def button_pressed(update, context):
    query = update.callback_query
    query.edit_message_text(text=query.data)

# TODO: REMEMBER TO REMOVE THIS SHIT
def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu