import hexchat
import random
import argparse
from collections import deque

__module_name__ = 'Slap script'
__module_author__ = 'ComputerTech'
__module_version__ = '0.7'
__module_description__ = 'Provides a /slap command for hexchat with non-repeating, customizable parts'

# Define the parts of the slap messages
VERBS = ["slaps", "whacks", "beats", "uses", "pokes", "smacks", "thumps", "bops", "wallops", "swats"]
PHRASES = ["around a bit", "something else here", "with all their might", "like a ragdoll", "gently", "furiously", "in jest", "for fun", "without mercy", "playfully"]
CONNECTORS = ["with a", "using a", "holding a", "armed with a", "brandishing a", "wielding a", "sporting a", "flaunting a", "equipped with a", "clutching a"]
ITEMS = ["large trout", "rubber chicken", "foam sword", "wet noodle", "giant flyswatter", "rolled-up newspaper", "plastic bat", "feather duster", "stuffed animal", "balloon animal"]

# Initialize queues for recently used parts
RECENT_VERBS = deque(maxlen=5)
RECENT_PHRASES = deque(maxlen=5)
RECENT_CONNECTORS = deque(maxlen=5)
RECENT_ITEMS = deque(maxlen=5)

def get_unique_part(part_list, recent_parts):
    part = random.choice(part_list)
    while part in recent_parts:
        part = random.choice(part_list)
    recent_parts.append(part)
    return part

def slap_command(word, word_eol, userdata):
    if len(word) < 2:
        hexchat.command("HELP slap")
        hexchat.prnt("Syntax: /slap <target> -a <amount> (-a is optional)")
        return hexchat.EAT_ALL

    parser = argparse.ArgumentParser()
    parser.add_argument("nick", help="the nickname of the person to slap")
    parser.add_argument("-a", "--amount", type=int, default=1, help="the number of times to slap the person")
    try:
        args = parser.parse_args(word[1:])
    except SystemExit:
        return hexchat.EAT_ALL

    for i in range(args.amount):
        verb = get_unique_part(VERBS, RECENT_VERBS)
        phrase = get_unique_part(PHRASES, RECENT_PHRASES)
        connector = get_unique_part(CONNECTORS, RECENT_CONNECTORS)
        item = get_unique_part(ITEMS, RECENT_ITEMS)
        message = f"{verb} {args.nick} {phrase} {connector} {item}"
        hexchat.command("me {}".format(message))

    return hexchat.EAT_ALL

def on_unload(userdata):
    hexchat.prnt("Slap script unloaded")

hexchat.hook_command("slap", slap_command)
hexchat.hook_unload(on_unload)

hexchat.prnt("Slap script loaded")
