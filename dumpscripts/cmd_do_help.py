# cmd_do_help.py

# Imposta gnureadline se readline è installato
try:
    import gnureadline
    import sys
    sys.modules['readline'] = gnureadline
except ImportError:
    pass

import cmd


class HelloWorld(cmd.Cmd):

    def do_greet(self, person):
        if person:
            print("salve,", person)
        else:
            print('salve')

    def help_greet(self):
        print('\n'.join([
            'greet [person]',
            'Saluta la persona con il nome ricevuto',
        ]))

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    HelloWorld().cmdloop()
