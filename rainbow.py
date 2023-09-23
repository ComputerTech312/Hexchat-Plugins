import hexchat
import itertools
import re

__module_name__ = "Rainbow"
__module_author__ = "ComputerTech"
__module_version__ = "1.0"
__module_description__ = "Rainbow stuff."

class RainbowPlugin:
    def __init__(self):
        self.COLORS_CYCLE = itertools.cycle([
            ('05', '10'), ('04', '12'), ('07', '02'), ('08', '06'),
            ('09', '13'), ('03', '15'), ('11', '14'), ('10', '05'),
            ('12', '04'), ('02', '07'), ('06', '08'), ('13', '09'),
            ('15', '03'), ('14', '11')
        ])
        self.PATTERN = re.compile(r'(\003\d\d?(,\d\d?)?|.)')
        self.commands = {
            "rainbow": self._rainbow,
            "rainbow2": self._rainbow2,
            "spoiler": self._spoiler,
        }
        for cmd, callback in self.commands.items():
            hexchat.hook_command(cmd, callback)
        hexchat.prnt('Rainbows script loaded')

    def _colorize_text(self, text, mode='rainbow'):
        result = []
        for char in self.PATTERN.findall(text):
            char = char[0]
            if char.startswith('\003'):
                result.append(char)
                continue
            if mode == 'rainbow':
                fg_color, _ = next(self.COLORS_CYCLE)
                result.append(f'\003{fg_color}{char}')
            elif mode == 'rainbow2':
                fg_color, bg_color = next(self.COLORS_CYCLE)
                result.append(f'\003{fg_color},{bg_color}{char}')
            elif mode == 'spoiler':
                result.append(f'\00314,14{char}')
        return ''.join(result)

    def _command_handler(self, word, word_eol, mode):
        hexchat.command(f'say {self._colorize_text(word_eol[1], mode)}')
        return hexchat.EAT_ALL

    def _rainbow(self, word, word_eol, _):
        return self._command_handler(word, word_eol, 'rainbow')

    def _rainbow2(self, word, word_eol, _):
        return self._command_handler(word, word_eol, 'rainbow2')

    def _spoiler(self, word, word_eol, _):
        return self._command_handler(word, word_eol, 'spoiler')

RainbowPlugin()
