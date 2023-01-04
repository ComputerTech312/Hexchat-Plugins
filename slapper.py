import hexchat
import random

__module_name__ = 'Slapper'
__module_author__ = 'ComputerTech'
__module_version__ = '0.1'
__module_description__ = 'Provides a /slap command for hexchat'

SLAP_MESSAGES = [
"slaps {nick} around a bit with a large trout",
"gives {nick} a good slap",
"slaps {nick} with a wet fish",
"slaps {nick} with a rolling pin",
"slaps {nick} with a newspaper",
"slaps {nick} around a bit with a small trout",
]

def slap_command(word, word_eol, userdata):
    if len(word) < 2:
        hexchat.command("HELP slap")
        return hexchat.EAT_ALL

    target = word[1]
    message = random.choice(SLAP_MESSAGES).format(nick=target)
    hexchat.command("me {}".format(message))

    return hexchat.EAT_ALL

def on_unload(userdata):
    hexchat.prnt("Slap script unloaded")

hexchat.hook_command("slap", slap_command)
hexchat.hook_unload(on_unload)

hexchat.prnt("Slap script loaded")
