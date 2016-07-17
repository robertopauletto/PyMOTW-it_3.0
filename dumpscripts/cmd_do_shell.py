#!/usr/bin/env python
# encoding: utf-8

import cmd
import os

class ShellEnabled(cmd.Cmd):
    
    last_output = ''

    def do_shell(self, line):
        "Esegue un comando di shell"
        print "esecuzione di un comando di shell:", line
        output = os.popen(line).read()
        print output
        self.last_output = output
    
    def do_echo(self, line):
        "Stampa l'input, sostituendo '$out' con l'output dell'ultimo comando di shell"
        # Ovviamente non robusto
        print line.replace('$out', self.last_output)
    
    def do_EOF(self, line):
        return True
    
if __name__ == '__main__':
    ShellEnabled().cmdloop()