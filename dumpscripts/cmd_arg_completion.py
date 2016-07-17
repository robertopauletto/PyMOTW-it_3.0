#!/usr/bin/env python
# encoding: utf-8

import cmd

class HelloWorld(cmd.Cmd):
    """Semplice esempio di processore di comando."""
    
    FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]
    
    def do_greet(self, person):
        "Saluta la persona"
        if person and person in self.FRIENDS:
            greeting = 'Ciao, %s!' % person
        elif person:
            greeting = "Salve, " + person
        else:
            greeting = 'Salve'
        print greeting
    
    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [ f
                            for f in self.FRIENDS
                            if f.startswith(text)
                            ]
        return completions
    
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()