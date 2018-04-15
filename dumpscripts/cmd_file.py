# cmd_file.py

import cmd


class HelloWorld(cmd.Cmd):

    # Disabilita l'uso del modulo rawinput
    use_rawinput = False

    # Non mostra il prompt dopo ogni lettura di comando
    prompt = ''

    def do_greet(self, line):
        print("Salve,", line)

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'rt') as input:
        HelloWorld(stdin=input).cmdloop()
