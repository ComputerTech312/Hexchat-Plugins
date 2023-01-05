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
"slaps {nick} around a bit with a soggy newspaper",
"slaps {nick} around the face with a baguette",
"slaps {nick} around a bit with a wet noodle",
"slaps {nick} around a bit with a foam sword",
"slaps {nick} around a bit with a banana peel",
"slaps {nick} with a copy of the IRC rulebook",
"slaps {nick} with a fresh baguette",
"slaps {nick} with a pillowy soft roll of bread dough",
"slaps {nick} with a bundle of herbs and spices",
"slaps {nick} with a jar of pickles",
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
