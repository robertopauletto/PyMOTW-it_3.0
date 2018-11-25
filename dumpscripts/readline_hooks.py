# readline_hooks.py

try:
    import gnureadline as readline
except ImportError:
    import readline


def startup_hook():
    readline.insert_text('da startup_hook')


def pre_input_hook():
    readline.insert_text(' da pre_input_hook')
    readline.redisplay()


readline.set_startup_hook(startup_hook)
readline.set_pre_input_hook(pre_input_hook)
readline.parse_and_bind('tab: complete')


while True:
    line = input('Prompt ("stop" per uscire): ')
    if line == 'stop':
        break
    print('DIGITATO: {!r}'.format(line))
