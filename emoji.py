__module_name__ = "Emoji"
__module_author__ = 'ComputerTech'
__module_version__ = "1.0"
__module_description__ = "Replaces various text strings with their corresponding emojis"

import hexchat
import re

# Define a dictionary that maps strings to emoji
emoji_dict = {
    ":eyes:": "👀",
    ":heart:": "❤️",
    ":smile:": "😊",
    ":joy:": "😂",
    ":clap:": "👏",
    ":thinking:": "🤔",
    ":ok_hand:": "👌",
    ":raised_hands:": "🙌",
    ":pray:": "🙏",
    ":fire:": "🔥",
    ":poop:": "💩",
    ":sunglasses:": "😎",
    ":thumbsup:": "👍",
    ":thumbsdown:": "👎",
    ":muscle:": "💪",
    ":moneybag:": "💰",
    ":gem:": "💎",
    ":crown:": "👑",
    ":gift:": "🎁",
    ":tada:": "🎉",
    ":balloon:": "🎈",
    ":beer:": "🍺",
    ":wine:": "🍷",
    ":pizza:": "🍕",
    ":hamburger:": "🍔",
    ":fries:": "🍟",
    ":cake:": "🎂",
    ":cookie:": "🍪",
    ":icecream:": "🍦",
    ":snowflake:": "❄️",
    ":umbrella:": "☂️",
    ":sun:": "☀️",
    ":star:": "⭐️",
    ":moon:": "🌙",
    ":cloud:": "☁️",
    ":rainbow:": "🌈",
    ":earth:": "🌍",
    ":phone:": "📱",
    ":computer:": "💻",
    ":key:": "🔑",
    ":lock:": "🔒",
    ":mailbox:": "📫",
    ":envelope:": "✉️",
    ":watch:": "⌚️",
    ":alarm:": "⏰",
    ":stopwatch:": "⏱️",
    ":hourglass:": "⏳",
    ":traffic:": "🚦",
    ":construction:": "🚧",
    ":hospital:": "🏥",
    ":hotel:": "🏨",
    ":bank:": "🏦",
    ":office:": "🏢",
}

def replace_emoji(word, word_eol, userdata):
    # Replace any matching strings with their corresponding emoji
    message = word[1]
    for key, value in emoji_dict.items():
        message = re.sub(re.escape(key), value, message)
    if message != word[1]:
        hexchat.command(f"say {message}")
        return hexchat.EAT_ALL
    return hexchat.EAT_NONE

# Register the "replace_emoji" function as a callback for messages
hexchat.hook_print("Channel Message", replace_emoji)
hexchat.hook_print("Your Message", replace_emoji)
