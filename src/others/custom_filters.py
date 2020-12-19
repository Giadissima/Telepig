from telegram.ext import MessageFilter

# return true if message is from a dm
class PrivateChatFilter(MessageFilter):
  def filter(self, message):
    return message.chat.type == "private"

# return true if message is from groups
class PublicChatFilter(MessageFilter):
  def filter(self, message):
    return message.chat.type == "supergroup" or message.chat.type == "group"

# inizialize filters' classes
Private = PrivateChatFilter()
Public = PublicChatFilter()