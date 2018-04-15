# cmd_arg_completion.py

# Imposta gnureadline come readline se installato.
try:
    import gnureadline
    import sys
    sys.modules['readline'] = gnureadline
except ImportError:
    pass

import cmd


class HelloWorld(cmd.Cmd):

    FRIENDS = ['Alice', 'Adam', 'Barbara', 'Bob']

    def do_greet(self, person):
        "Saluta la persona"
        if person and person in self.FRIENDS:
            greeting = 'Ciao, {}!'.format(person)
        elif person:
            greeting = 'Salve, {}'.format(person)
        else:
            greeting = 'Salve'
        print(greeting)

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [
                f
                for f in self.FRIENDS
                if f.startswith(text)
            ]
        return completions

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    HelloWorld().cmdloop()
