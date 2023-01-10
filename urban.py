import hexchat
import requests

__module_name__ = 'Urban Dictionary script'
__module_author__ = 'ComputerTech'
__module_version__ = '0.3'
__module_description__ = 'Provides a /define command for hexchat which uses the Urban Dictionary API.'

def define(word, word_eol, userdata):
    query = word[1]
    if "--all" in word:
        show_all = True
        query = query.replace("--all", "").strip()
    else:
        show_all = False
    r = requests.get("http://api.urbandictionary.com/v0/define?term={}".format(query))
    if r.status_code != 200:
        hexchat.prnt("Error: API request failed with status code {}".format(r.status_code))
        return hexchat.EAT_ALL
    data = r.json()
    if "error" in data:
        hexchat.prnt("Error: {}".format(data["error"]))
        return hexchat.EAT_ALL
    if show_all:
        definitions = [entry["definition"] for entry in data["list"]]
        hexchat.prnt("{}:".format(query))
        for i, definition in enumerate(definitions):
            hexchat.prnt("  {}. {}".format(i+1, definition))
    else:
        definition = data["list"][0]["definition"]
        hexchat.prnt("{}: {}".format(query, definition))
    
    return hexchat.EAT_ALL


def on_unload(userdata):
    hexchat.prnt("Urban Dictionary script unloaded")

hexchat.hook_command("define", define, help="/define <word> [--all] - Looks up the definition of a word using Urban Dictionary. Use --all to display all definitions.")
hexchat.hook_unload(on_unload)

hexchat.prnt("Urban Dictionary script loaded")
