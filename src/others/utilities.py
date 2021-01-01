
#*---------------------------*#
#*         BOT UTILS         *#
#*---------------------------*#
def get_username(update):
  """
  Function to retrive username

  Returns
  -------
  Return string or None type if the user
  doesn't have a username.
  """
  return update.message.from_user['username']

def get_user_id(update):
  """
  Function to retrive telegram user id
  """
  return update.message.from_user['id']

#*---------------------------*#
#*     DISPATCHER UTILS      *#
#*---------------------------*#

def loadHandlers(dispatcher, handlers):
  """
  This function add to dispatchers an array of handlers
  """
  for handler in handlers:
    dispatcher.add_handler(handler)