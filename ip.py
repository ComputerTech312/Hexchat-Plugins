import hexchat
import requests

__module_name__ = "IP Lookup"
__module_author__ = "ComputerTech"
__module_version__ = "1.0"

def ip_lookup(ip, fields):
    if fields == "all":
        url = f"http://ip-api.com/json/{ip}"
    else:
        url = f"http://ip-api.com/json/{ip}?fields={fields}"
    response = requests.get(url)
    data = response.json()
    if 'status' in data and data["status"] == "success":
        output = ""
        for key, value in data.items():
            output += f"{key}: {value}\n"
        return output
    else:
        return "Could not retrieve location information."

def ip_lookup_cb(word, word_eol, userdata):
    if len(word) < 2:
        hexchat.prnt("Please provide an IP address to look up.")
        return hexchat.EAT_ALL

    ip = word[1]
    fields = ",".join(word[2:]) if len(word) > 2 else "country,city"
    location = ip_lookup(ip, fields)
    hexchat.prnt(f"Location for IP {ip}: {location}")
    return hexchat.EAT_ALL

hexchat.hook_command("IPLOOKUP", ip_lookup_cb, help="/IPLOOKUP <ip> [fields] - Look up the location of an IP address using the ip-api service. Fields is a comma-separated list of fields to retrieve, e.g. 'country,regionName,city'. Use 'all' to retrieve all available fields. The default fields are 'country' and 'city'.")

hexchat.prnt(f"{__module_name__} version {__module_version__} by {__module_author__} loaded.")
