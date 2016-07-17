#!/usr/bin/env python
# encoding: utf-8

import cmd

class HelloWorld(cmd.Cmd):
    """Semplice esempio di processore di comando."""
    
    def do_greet(self, person):
        """greet [persona]
        Saluta la persona"""
        if person:
            print "ciao,", person
        else:
            print 'ciao'
    
    def do_EOF(self, line):
        return True
    
    def postloop(self):
        print

if __name__ == '__main__':
    HelloWorld().cmdloop()

