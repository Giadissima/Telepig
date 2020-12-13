import json
from os.path import isfile, abspath, join
from src.exceptions import NoLanguageFoundException

"""
POKEMON  #raid 
⏰ Ora

📝 gay

⚔️Host: @Giadissima1234 [nickname] livello 34
friendcode: 000 000 000 000

📡 Partecipanti da remoto: 
"""

def parse_text(message_code, args):
    RAID_TEXT = "{} #raid \n⏰ {}\n\n📝 {}\n\n⚔️Host: {} {} livello {}\n"
    RAID_TEXT += "friendcode: {}\n\n📡 Partecipanti da remoto:"
    # messages
    if message_code == "RAID_TEXT":
        # @par pokemon, raid time, notes, username, nickname, friendcode
        return RAID_TEXT.format(*args)

# Example:
# get_message("RAID_MESSAGE", lang="en")
# TODO: TEST
def get_message(message_code, args = (), lang = "it"):
    LANGUAGES_PATH = "./languages"

    filename = abspath(join(LANGUAGES_PATH, lang+".json"))
    if not isfile(filename): abspath(join(LANGUAGES_PATH,"en.json"))

    ALL_MESSAGES = {}
    with open(filename) as f:
        ALL_MESSAGES = json.loads(f)

    if not message_code in ALL_MESSAGES: raise NoLanguageFoundException()

    message_to_return = ALL_MESSAGES[message_code] % args
    return message_to_return