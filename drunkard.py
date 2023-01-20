import hexchat
import random

__module_name__ = "Drunkard"
__module_version__ = "1.1"
__module_description__ = "Makes text appear as if it's typed by someone who is drunk and with typos"

def drunk_text(word, word_eol, userdata):
    text = word_eol[1]
    if text:
        # randomly change some letters to uppercase
        new_text = ''.join(c.upper() if random.random() < 0.5 else c for c in text)

        # introduce typos randomly
        typos = ['u','i','e','a','o','s','n','r','h','l','t','d','c','m','p','b','g','f','y','w','k','j','v','x','q','z']
        for i in range(int(len(new_text)/5)):
            if random.random() < 0.1:
                new_text = new_text[:random.randint(0, len(new_text)-1)] + random.choice(typos) + new_text[random.randint(0, len(new_text)-1):]
        hexchat.command("say {}".format(new_text))
    else:
        hexchat.command("help drunk")

hexchat.hook_command("drunk", drunk_text, help="/drunk [text] - Outputs text as if typed by someone who is drunk and with typos")

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded.")
