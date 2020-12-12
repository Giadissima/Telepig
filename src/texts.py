"""
POKEMON  #raid 
⏰ Ora

📝 gay

⚔️Host: @Giadissima1234 [nickname] livello 34
friendcode: 000 000 000 000

📡 Partecipanti da remoto: 
"""


def parse_text(message_code, args*):
    # messages
    RAID_TEXT = "{} #raid \n⏰ {}\n\n📝 {}\n\n⚔️Host: {} {} livello {}\nfriendcode: {}\n\n📡 Partecipanti da remoto:"
    if message_code == "RAID_TEXT":
        # @par pokemon, raid time, notes, username, nickname, friendcode
        return RAID_TEXT.format(args[0], args[1], args[2], args[3], args[4])