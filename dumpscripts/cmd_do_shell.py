# cmd_do_shell.py

import cmd
import subprocess


class ShellEnabled(cmd.Cmd):

    last_output = ''

    def do_shell(self, line):
        "Esegue un comando shell"
        print("esecuzione di comando shell:", line)
        sub_cmd = subprocess.Popen(line,
                                   shell=True,
                                   stdout=subprocess.PIPE)
        output = sub_cmd.communicate()[0].decode('utf-8')
        print(output)
        self.last_output = output

    def do_echo(self, line):
        """Stampa l'input, sostituendo '$out' con
        l'output dell'ultimo comando shell
        """
        # Ovviamente non robusto
        print(line.replace('$out', self.last_output))

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    ShellEnabled().cmdloop()
