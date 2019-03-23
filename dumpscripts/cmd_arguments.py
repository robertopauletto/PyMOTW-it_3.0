# cmd_arguments.py

import cmd


class HelloWorld(cmd.Cmd):

    def do_greet(self, person):
        """greet [person]
        Saluta la persona"""
        if person:
            print("Salve,", person)
        else:
            print('Salve')

    def do_EOF(self, line):
        return True

    def postloop(self):
        print()


if __name__ == '__main__':
    HelloWorld().cmdloop()
