
def rDNS(word, word_eol, userdata):
    if len(word) < 2:
        print("Error: No IP address provided")
        return

    ip_address = word[1]
    dns_result = hexchat.command("dns {}".format(ip_address))
    print("rDNS for {}: {}".format(ip_address, dns_result))
    
hexchat.hook_command("rDNS", rDNS)
