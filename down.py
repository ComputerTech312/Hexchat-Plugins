import hexchat

__module_name__ = "DOP Plugin"
__module_author__ = "ComputerTech"
__module_version__ = "1.0"
__module_description__ = "Removes all current status in the current channel when '/down' is typed"

def down_callback(word, word_eol, userdata):
    channel = hexchat.get_info("channel")
    prefixes = hexchat.get_prefs("irc_extra_prefixes")

    if "~" in prefixes:
        hexchat.command("cs deowner " + channel + " " + hexchat.get_info("nick"))
    elif "&" in prefixes:
          hexchat.command("cs deprotect " + channel + " " + hexchat.get_info("nick"))
    elif "@" in prefixes:
          hexchat.command("cs deop " + channel + " " + hexchat.get_info("nick"))
    elif "%" in prefixes:
          hexchat.command("cs dehalfop " + channel + " " + hexchat.get_info("nick"))#
    elif "+" in prefixes:
          hexchat.command("cs deop " + channel + " " + hexchat.get_info("nick"))
    
    return hexchat.EAT_ALL

hexchat.hook_command("DOWN", down_callback) 
