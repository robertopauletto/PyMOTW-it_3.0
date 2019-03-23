# warnings_formatwarning.py

import warnings


def warning_on_one_line(message, category, filename, lineno,
                        file=None, line=None):
    return '-> {}:{}: {}:{}'.format(
        filename, lineno, category.__name__, message)


warnings.warn('Messaggio di avvertimento, prima')
warnings.formatwarning = warning_on_one_line
warnings.warn('Messaggio di avvertimento, dopo')
