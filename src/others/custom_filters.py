from telegram.ext import MessageFilter

class PrivateChatFilter(MessageFilter):
  """
  Filters for private chats only
  """
  def filter(self, message):
    return message.chat.type == "private"

class PublicChatFilter(MessageFilter):
  """
  Filters for group/supergroup chats only
  """
  def filter(self, message):
    return message.chat.type == "supergroup" or message.chat.type == "group"

# Inizialize filters' classes
Private = PrivateChatFilter()
Public = PublicChatFilter()