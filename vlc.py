import hexchat, requests, os
from requests.exceptions import RequestException
from json import JSONDecodeError

__module_name__ = 'VLC'
__module_author__ = 'ComputerTech'
__module_version__ = '0.1'
__module_description__ = 'Fetches and displays the current playing status from VLC media player'

VLC_HTTP_PASSWORD = 'password'  # Replace with your VLC HTTP password
VLC_HTTP_URL = 'http://localhost:8080/requests/status.json'  # Default VLC HTTP interface URL

MSG_PLAYING = '\002Now playing:\002 {} | \002Length:\002 {} seconds | \002Current position:\002 {} seconds'
MSG_NOTHING_PLAYING = 'SAY \002Nothing is currently playing in VLC.\002'
MSG_UNKNOWN_STATE = 'SAY \002VLC is not in a known state.\002'
MSG_ERROR = 'Error communicating with VLC: {}'

def get_vlc_status():
    try:
        response = requests.get(VLC_HTTP_URL, auth=('', VLC_HTTP_PASSWORD))
        response.raise_for_status()
        return response.json()
    except (RequestException, JSONDecodeError) as e:
        print(MSG_ERROR.format(e))
        return None

def format_time(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    return f"{minutes:02d}:{seconds:02d}"

def get_now_playing(word, word_eol, userdata):
    data = get_vlc_status()
    if data is None:
        return hexchat.EAT_ALL

    state = data.get('state')
    now_playing = data.get('information', {}).get('category', {}).get('meta', {}).get('title')
    if now_playing:
        now_playing = os.path.splitext(now_playing)[0]  # Remove any file extension from the song name
    length = format_time(data.get('length', 0))
    time = format_time(data.get('time', 0))

    if state == 'playing' and now_playing:
        hexchat.command(f'SAY {MSG_PLAYING.format(now_playing, length, time)}')
    elif state == 'paused':
        hexchat.command(MSG_NOTHING_PLAYING)
    else:
        hexchat.command(MSG_UNKNOWN_STATE)

    return hexchat.EAT_ALL

def on_unload(userdata):
    print(f'{__module_name__}, {__module_version__} has been unloaded')

hexchat.hook_command('np', get_now_playing, help='Use /np to fetch and display the current playing status from VLC.')
hexchat.hook_unload(on_unload)
print(f' {__module_name__}, {__module_version__} loaded.')
