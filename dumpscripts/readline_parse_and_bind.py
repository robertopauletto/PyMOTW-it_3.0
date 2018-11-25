# readline_parse_and_bind.py


try:
    import gnureadline as readline
except ImportError:
    import readline

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')

while True:
    line = input('Prompt ("stop" per abbandonare): ')
    if line == 'stop':
        break
    print('DIGITATO: {!r}'.format(line))
