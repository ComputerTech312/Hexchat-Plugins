import hexchat
import random

__module_name__ = "Random Emoji/ASCII Art from File"
__module_version__ = "1.0"
__module_description__ = "Sends a random emoji or ASCII art from a file to the chat"

# Path to your file containing the emojis and ASCII arts
file_path = "/your/path/here/hexchat/addons/emoticons.tsv"

def load_emojis_from_file():
    emojis = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Find the tab character and keep only the part before it
            emoji = line.split('\t')[0]
            emojis.append(emoji)
    return emojis

emojis_ascii = load_emojis_from_file()

def send_random_emoji(word, word_eol, userdata):
    random_emoji = random.choice(emojis_ascii)
    # Send the selected item to the current channel or query
    hexchat.command(f"MSG {hexchat.get_info('channel')} {random_emoji}")
    return hexchat.EAT_ALL

# Register the command with HexChat
hexchat.hook_command("randemoji", send_random_emoji, help="/RANDMOJI to send a random emoji or ASCII art from file")

print(f"{__module_name__} version {__module_version__} loaded.")
