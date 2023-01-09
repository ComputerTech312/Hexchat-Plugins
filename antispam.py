import hexchat

__module_name__ = "Anti-Spam Plugin"
__module_author__ = "ComputerTech"
__module_version__ = "1.0"
__module_description__ = "This plugin blocks specific words in channels and private messages."

# Spam keywords to be blocked
spam_keywords = ["viagra", "cialis", "poker", "casino", "loans", "mortgage", "refinance", "insurance"]

# Function to check for spam
def is_spam(text):
  for keyword in spam_keywords:
    if keyword in text.lower():
      return True
  return False

# Callback function for PRIVMSG event
def private_message_cb(word, word_eol, userdata):
  if is_spam(word_eol[1]):
    # Block the message
    return hexchat.EAT_ALL
  return hexchat.EAT_NONE

# Callback function for CHAT event
def channel_message_cb(word, word_eol, userdata):
  if is_spam(word_eol[1]):
    # Block the message
    return hexchat.EAT_ALL
  return hexchat.EAT_NONE

# Hook PRIVMSG and CHAT events
hexchat.hook_print("Private Message", private_message_cb)
hexchat.hook_print("Channel Message", channel_message_cb)

print(f"{__module_name__} version {__module_version__} loaded.") 
