#!/usr/bin/env python
# encoding: utf-8

import cmd

class HelloWorld(cmd.Cmd):
    """Semplice esempio di processore di comando."""

    prompt = 'prompt: '
    intro = "Semplice esempio di processore di comando."

    doc_header = 'doc_header'
    misc_header = 'misc_header'
    undoc_header = 'undoc_header'
    
    ruler = '-'
    
    def do_prompt(self, line):
        "Cambia il prompt interattivo"
        self.prompt = line + ': '

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()