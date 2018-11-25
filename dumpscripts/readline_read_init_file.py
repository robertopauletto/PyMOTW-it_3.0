# readline_read_init_file.py


try:
    import gnureadline as readline
except ImportError:
    import readline

readline.read_init_file('myreadline.rc')

while True:
    line = input('Prompt ("stop" per abbandonare): ')
    if line == 'stop':
        break
    print('DIGITATO: {!r}'.format(line))
