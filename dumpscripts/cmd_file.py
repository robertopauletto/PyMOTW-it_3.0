#!/usr/bin/env python
# encoding: utf-8

import cmd

class HelloWorld(cmd.Cmd):
    """Semplice esempio di processore di comando."""
    
    # Disabilita l'uso del modulo rawinput module
    use_rawinput = False
    
    # Non mostra il prompt dopo ogni lettura di comando
    prompt = ''
    
    def do_greet(self, line):
        print "Salve,", line
    
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    import sys
    input = open(sys.argv[1], 'rt')
    try:
        HelloWorld(stdin=input).cmdloop()
    finally:
        input.close()
        