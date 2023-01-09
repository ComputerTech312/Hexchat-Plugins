import hexchat
import requests

__module_name__ = 'Urban Dictionary script'
__module_author__ = 'ComputerTech'
__module_version__ = '0.1'
__module_description__ = 'Provides a /define command for hexchat which uses the Urban Dictionary API.'


def define(word, word_eol, userdata):
    query = word[1]
    r = requests.get("http://api.urbandictionary.com/v0/define?term={}".format(query))
    data = r.json()
    definition = data["list"][0]["definition"]
    hexchat.prnt("{}: {}".format(query, definition))
    
    return hexchat.EAT_ALL


def on_unload(userdata):
    hexchat.prnt("Urban Dictionary script unloaded")

hexchat.hook_command("define", define, help="/define <word> - Looks up the definition of a word using Urban Dictionary")
hexchat.hook_unload(on_unload)

hexchat.prnt("Urban Dictionary script loaded")
