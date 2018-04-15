# cmd_do_help.py

# Imposta nureadline se readline è installato
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
            print("ciao,", person)
        else:
            print('ciao')

    def help_greet(self):
        print('\n'.join([
            'greet [person]',
            'Saluta la persona passata',
        ]))

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    HelloWorld().cmdloop()
