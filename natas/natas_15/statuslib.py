from datetime import datetime as date

class Imprinter:

    def __init__(self, string, code='info', text=False, logging=False, customize=None):
        self.string = string
        self.name = code
        self.customize = customize
        self.logging = logging
        self.text = text
        self.time = date.now().strftime("%Y-%m-%d %H:%M:%S")

        self.art = dict(
            log='[v]',
            info='[i]',
            success='[+]',
            failed='[-]',
            working='[*]',
            warning='[!]',
            prompt='[>]',
            shell='[$]',
            root='[#]',
        )

        self.log = dict(
            log='[LOG]:',
            info='[INFO]:',
            success='[SUCCESS]:',
            failed='[FAILED]:',
            working='[WORKING]:',
            warning='[WARNING]:',
            prompt='[PROMPT]',
        )

    def _print_class(self, **kwargs):
        art, log, used, string = kwargs['art'], kwargs['log'], kwargs['used'], kwargs['string']

        return ('<Status Art: %s>\n<Status Text: %s>\n<Used: %s>\n<String: %s>' % (art,
                                                                                   log,
                                                                                   used,
                                                                                   string))

    def __str__(self):

        if self.name is None:
            return '<Status Art: %s>\n<Status Text: %s>\n<Used: None>\n<String: %s>' % (self.art,
                                                                                        self.log,
                                                                                        self.string)

        else:

            if self.text is False:
                return self._print_class(art=self.art,
                                         log=self.log,
                                         used=self.art[self.name],
                                         string=self.string
                                         )

            else:
                return self._print_class(art=self.art,
                                         log=self.log,
                                         used=self.log[self.name],
                                         string=self.string
                                         )

    def _imprint_handler(self, **kwargs):
        customize = kwargs['customize']
        name = kwargs['name']
        text = kwargs['text']
        string = kwargs['string']
        logging = kwargs['logging']
        raw = kwargs['raw']
        art = self.art
        log = self.log
        time = '%s%s%s' % ('[', self.time, ']')

        # print(kwargs)
        # import sys
        # sys.exit()

        # Return values from art or log
        def iterobj_handler(name, text, string, logging, dic):

            for item, value in dic.items():

                if name is None and logging is True:
                    return time, string

                if name == item and logging is False:
                    return value, string

                if name == item and logging is True:
                    return value, time, string

                if name is None:
                    return string

                if name not in dic:
                    raise ValueError('Keyword value is not in the list')

        # Imprint method
        if raw is False:

            if customize:
                raise TypeError('Unexpected customized keyword argument')

            if name is None and logging is True:
                return (' '.join(str(value) for value in self.raw_imprint()))

            if name is None:
                return string

            else:
                return (' '.join(str(value) for value in self.raw_imprint()))

        # Raw Imprint method
        else:

            if customize:
                raise TypeError('Unexpected customized keyword argument.')

            if name and text is False:

                # Char / Art indicators value
                return iterobj_handler(name, text, string, logging, art)

            if name and text is True:

                # Text indicators value
                return iterobj_handler(name, text, string, logging, log)

            if name is None and logging is True:

                # Timestamp logging without indicators
                return iterobj_handler(name, text, string, logging, log)

            if name is None and logging is False:

                if text is True:
                    return iterobj_handler(name, text, string, logging, log)

                else:
                    return iterobj_handler(name, text, string, logging, log)

    def imprint(self):

        return self._imprint_handler(customize=self.customize,
                                     name=self.name,
                                     text=None,
                                     string=self.string,
                                     logging=self.logging,
                                     raw=False)

    def raw_imprint(self):
        return self._imprint_handler(customize=self.customize,
                                     name=self.name,
                                     text=self.text,
                                     string=self.string,
                                     logging=self.logging,
                                     raw=True
                                     )

    def _customizer(self, **kwargs):

        # Handler for customized imprinter methods

        customize = kwargs['customize']
        text = kwargs['text']
        string = kwargs['string']
        logging = kwargs['logging']
        time = '%s%s%s' % ('[', self.time, ']')

        def customizer_handler(customize, text, string):

            if text is True:
                try:
                    if len(customize) > 8 or len(customize) < 2:
                        raise ValueError('Keyword text=True: Message must be at least 2 to 10 characters.')

                    if string and logging is False:
                        return ('[%s]: %s' % (customize, string))

                    if string and logging is True:
                        return ('[%s]: %s %s' % (customize, time, string))

                    else:
                        return ('[%s]' % (customize))

                except TypeError:
                    raise ValueError('Keyword customize does not support None-type')

            else:
                try:
                    if len(customize) > 1 or len(customize) < 1:
                        raise ValueError('Keyword text=False: Indicator must be at least 1 character.')

                    if string and logging is False:
                        return ('[%s] %s' % (customize, string))

                    if string and logging is True:
                        return ('[%s] %s %s' % (customize, time, string))

                    else:
                        return ('[%s]' % (customize))

                except TypeError:
                    raise ValueError('Keyword customize does not support None-type')

        return customizer_handler(customize, text, string)

    # Customized imprinter methods

    def custom_imprint(self):
        return self._customizer(string=self.string,
                                customize=self.customize,
                                text=self.text,
                                logging=self.logging
                                )

    def custom_code(self):
        return self._customizer(string=None,
                                customize=self.customize,
                                text=self.text,
                                logging=self.logging
                                )


class Colorizer:

    def __init__(self, string, color):
        self.string = string
        self.name = color
        self.reset = '\033[0;0m'

        self.colors = dict(
            cyan='\033[0;96m',
            green='\033[0;92m',
            red='\033[0;91m',
            purple='\033[0;95m',
            yellow='\033[0;93m',
            blue='\033[0;94m',
            gray='\033[0;90m',
            white='\033[0;97m',

            # Bold Colors

            b_cyan='\033[1;96m',
            b_green='\033[1;92m',
            b_red='\033[1;91m',
            b_puple='\033[1;95m',
            b_yellow='\033[1;93m',
            b_blue='\033[1;94m',
            b_gray='\033[1;90m',
            b_white='\033[1;97m',
        )

    def __str__(self):
        return ('<Color Pallete: %s>\n<Color Used: %s%s%s>\n<String: %s>' % (self.colors,
                                                                             self.colors[self.name],
                                                                             self.name,
                                                                             self.reset,
                                                                             self.string
                                                                             ))

    def _selector(self, obj):

        for item, value in obj.items():
            if self.name == item:
                return ('%s%s%s' % (value, self.string, self.reset))

            if self.name not in obj:
                raise ValueError('Value is not in the list')

    def colorize(self):
        return self._selector(self.colors)


class status:

    ''' Static method '''

    def _handler(message, **kwargs):

        code = kwargs['code']
        text = kwargs['text']
        logging = kwargs['logging']
        color = kwargs['color']

        def is_logging(message, code, text, logging, color):

            if logging is False:

                imprinter = Imprinter(message, code=code, text=text, logging=logging)
                logger, string = imprinter.raw_imprint()

                colorizer = Colorizer(logger, color=color)
                return ('%s %s' % (colorizer.colorize(), string))

            if logging is True:

                imprinter = Imprinter(message, code=code, text=text, logging=logging)
                logger, time, string = imprinter.raw_imprint()

                colorizer = Colorizer(logger, color=color)
                return ('%s %s %s' % (colorizer.colorize(), time, string))

        print(is_logging(message, code, text, logging, color))

    # Default status indicator methods

    def log(message, code='info', color='gray', text=False, logging=False):
        status._handler(message, code=code, color=color, text=text, logging=logging)

    def info(message, text=False, logging=False):
        status._handler(message, code='info', color='cyan', text=text, logging=logging)

    def success(message, text=False, logging=False):
        status._handler(message, code='success', color='green', text=text, logging=logging)

    def failed(message, text=False, logging=False):
        status._handler(message, code='failed', color='red', text=text, logging=logging)

    def working(message, text=False, logging=False):
        status._handler(message, code='working', color='purple', text=text, logging=logging)

    def warning(message, text=False, logging=False):
        status._handler(message, code='warning', color='yellow', text=text, logging=logging)
