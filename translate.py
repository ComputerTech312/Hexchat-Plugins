import hexchat
import requests

__module_name__ = "Translate"
__module_version__ = "1.0"
__module_description__ = "Perform text translation on a message using the /translate command using Google Translate API."

api_key = 'your_api_key'

def translate_cb(word, word_eol, userdata):
    if len(word) < 3:
        hexchat.prnt("Not enough arguments. Usage: /translate [text] [target_language]")
        return hexchat.EAT_ALL
    text = word_eol[1]
    target = word[2]

    url = 'https://translation.googleapis.com/language/translate/v2'
    data = {
        'q': text,
        'target': target,
        'key': api_key
    }
    r = requests.post(url, json=data)

    translation = r.json()['data']['translations'][0]['translatedText']

    hexchat.prnt("Translation: {}".format(translation))

    return hexchat.EAT_ALL
  
hexchat.hook_command("translate", translate_cb)
hexchat.prnt("TextTranslator plugin loaded.")
