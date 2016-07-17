#!/usr/bin/env python
# encoding: utf-8

import cmd

class InteractiveOrCommandLine(cmd.Cmd):
    """Accetta comandi tramite il normale prompt interattivo o da riga di comando"""
    
    def do_greet(self, line):
        print 'Salve,', line
    
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        InteractiveOrCommandLine().onecmd(' '.join(sys.argv[1:]))
    else:
        InteractiveOrCommandLine().cmdloop()