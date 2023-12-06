import hexchat
import sys

# Add the lib directory to the system path
sys.path.append('/your/path/here/.config/hexchat/addons/lib-large')

# Now import text2art from the art library inside the lib folder
from art61.art import text2art

__module_name__ = "ASCII Art Text"
__module_version__ = "1.0"
__module_description__ = "Converts text to ASCII art using tarty3 font"

def large_text(word, word_eol, userdata):
    if len(word) > 1:
        # Combine the words into a single string and generate ASCII art using the tarty3 font
        input_text = ' '.join(word[1:])
        ascii_art = text2art(input_text, font='tarty4')  # Specify the tarty3 font here
        
        # Send each line of the ASCII art as a separate message
        for line in ascii_art.split('\n'):
            hexchat.command(f"say {line}")
    else:
        hexchat.prnt("Usage: /large <text>")
    return hexchat.EAT_ALL

# Hook the /large command
hexchat.hook_command("large", large_text, help="/large <text> - Converts text to ASCII art using tarty3 font")

print(f"{__module_name__} version {__module_version__} loaded.")
