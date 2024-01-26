import hexchat

__module_name__ = 'Flipper'
__module__author__ = 'ComputerTech'
__module_version__ = '1.0'
__module_description__ = 'Flips your text upside down'

FLIP_TABLE = {
    'a': '\u0250', 'b': 'q', 'c': '\u0254', 'd': 'p', 'e': '\u01DD', 'f': '\u025F', 
    'g': '\u0183', 'h': '\u0265', 'i': '\u0131', 'j': '\u027E', 'k': '\u029E', 
    'l': '\u0283', 'm': '\u026F', 'n': 'u', 'o': 'o', 'p': 'd', 'q': 'b', 'r': '\u0279', 
    's': 's', 't': '\u0287', 'u': 'n', 'v': '\u028C', 'w': '\u028D', 'x': 'x', 'y': '\u028E', 
    'z': 'z', '.': '\u02D9', '[': ']', ']': '[', '(': ')', ')': '(', '{': '}', '}': '{', 
    '?': '\u00BF', '!': '\u00A1', "\'": ',', ',': "\'", '<': '>', '>': '<', '_': '\u203E', 
    ';': '\u061B', '9': '6', '6': '9',
    'A': '\u2200', 'B': 'q', 'C': '\u0186', 'D': 'p', 'E': '\u018E', 'F': '\u2132', 
    'G': '\u05e4', 'H': 'H', 'I': 'I', 'J': '\u017F', 'K': '\u22CA', 'L': '\u02E5', 
    'M': 'W', 'N': 'N', 'O': 'O', 'P': 'd', 'Q': '\u038C', 'R': '\u1D1A', 'S': 'S', 
    'T': 'T', 'U': '\u2229', 'V': '\u039B', 'W': 'M', 'X': 'X', 'Y': '\u2144', 'Z': 'Z'
}

def flip_text(word, word_eol, userdata):
    text = word_eol[1]
    try:
        flipped_text = ''.join(FLIP_TABLE.get(c, c) for c in reversed(text))
        hexchat.command("say {}".format(flipped_text))
    except Exception as e:
        hexchat.prnt("Error flipping text: {}".format(str(e)))
    return hexchat.EAT_ALL

def check_unsupported_chars(word, word_eol, userdata):
    text = word_eol[1]
    unsupported_chars = set(text) - set(FLIP_TABLE.keys())
    if unsupported_chars:
        hexchat.prnt("Warning: The following characters are not supported and will not be flipped: {}".format(", ".join(unsupported_chars)))

def on_unload(userdata):
    print(f'{__module_name__}, {__module_version__} has been unloaded')

hexchat.hook_command('flip', flip_text, help='Use /flip to flip your text.')
hexchat.hook_command('flip', check_unsupported_chars)
print(f' {__module_name__}, {__module_version__} loaded.')
