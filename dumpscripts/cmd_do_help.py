#!/usr/bin/env python
# encoding: utf-8

import cmd

class HelloWorld(cmd.Cmd):
    """Semplice esempio di processore di comando."""
    
    def do_greet(self, person):
        if person:
            print "ciao,", person
        else:
            print 'ciao'
    
    def help_greet(self):
        print '\n'.join([ 'greet [persona]',
                           'Saluta la persona',
                           ])
    
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()