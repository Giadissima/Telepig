# return none if the username doesn't exist
def get_username(update):
    return update.message.from_user['username']

def get_user_id(update):
    return update.message.from_user['id']