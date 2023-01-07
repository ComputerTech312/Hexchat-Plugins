import hexchat
import random
import argparse

__module_name__ = 'Slap script'
__module_author__ = 'ComputerTech'
__module_version__ = '0.2'
__module_description__ = 'Provides a /slap command for hexchat with an optional -a option to specify the number of slaps'

SLAP_MESSAGES = [
"slaps {nick} around a bit with a large trout",
"gives {nick} a good slap",
"slaps {nick} with a wet fish",
"slaps {nick} with a rolling pin",
"slaps {nick} with a newspaper",
"slaps {nick} around a bit with a small trout",
"gives {nick} a swift slap across the face",
"wallops {nick} with a giant flyswatter",
"delivers a powerful slap to {nick}'s cheek",
"slaps {nick} with a wet noodle",
"sends {nick} flying with a mighty slap",
"rounds up a group of seagulls to attack {nick} with a series of sharp pecks and slaps",
]

def slap_command(word, word_eol, userdata):
    # If no arguments were provided, display a syntax error message
    if len(word) < 2:
        hexchat.command("HELP slap")
        hexchat.prnt("Syntax: /slap <target> -a <amount> (-a is optional)")
        return hexchat.EAT_ALL

    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("nick", help="the nickname of the person to slap")
    parser.add_argument("-a", "--amount", type=int, default=1, help="the number of times to slap the person")
    try:
        args = parser.parse_args(word[1:])
    except SystemExit:
        return hexchat.EAT_ALL

    # Send the specified number of slap messages
    for i in range(args.amount):
        message = random.choice(SLAP_MESSAGES).format(nick=args.nick)
        hexchat.command("me {}".format(message))

    return hexchat.EAT_ALL

def on_unload(userdata):
    hexchat.prnt("Slap script unloaded")

hexchat.hook_command("slap", slap_command)
hexchat.hook_unload(on_unload)

hexchat.prnt("Slap script loaded")
