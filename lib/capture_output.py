#!/usr/bin/env python
# -*- coding: utf-8 -*-
# capture_output.py

import subprocess
import os

__doc__ = """
Cattura l'output degli script di esempio

L'idea è di non inserire il risultato degli script nella pagina html con 
copia/incolla ma dinamicamente eseguendo lo script stesso. 
"""
__version__ = "0.1"
__changelog__ = """

"""


class CaptureOutputScript(object):
    """Cattura l'output degli script di esempio

    L'idea è di non inserire il risultato degli script nella pagina html con
    copia/incolla ma dinamicamente eseguendo lo script stesso.
    """
    def __init__(self, pycmd=None, shellcmd=None):
        """([str] [,str])

        prerequisito: se `pycmd` non è nel PATH occorre passare il percorso
        completo

        :param pycmd: Il nome dell'interprete Python da eseguire (def. python3)
        :param shellcmd: Il nome della console da chiamare (def. /bash)
        """
        self._output = list()
        self._pycommand = "python3" or pycmd
        self._shell_cmd = '/bin/bash' or shellcmd

    def _create_shell_script(self, script, path):
        """(str [,str]) -> str

        Crea un file bash con all'interno il codice per eseguire `script` con
        l'interprete python definito nell'istanza della classe

        :param script: il nome dello script python da eseguire
        :param path: il percorso su cui scrivere il file bash
        :return: il nome dello script bash da eseguire
        """
        if path:
            script_name = os.path.join(os.path.abspath(path), '_pyrunner.sh')
        else:
            script_name = os.path.abspath('_pyrunner.sh')
        code = [
            "#!/usr/bin/env bash",
            "{} {}\n".format(self._pycommand, os.path.abspath(script))
        ]
        with open(script_name, mode='w') as fh:
            fh.write('\n'.join(code))
        return script_name

    def run(self, script, path=None):
        """(str [,str] -> str

        Crea uno script bash al cui interno inserisce uno script python da
        eseguire.

        :param script: il nome dello script python da eseguire
        :param path: il percorso su cui scrivere il file bash
        :return: l'output del comando o l'eventuale errore verificatosi
        """
        sh_script = self._create_shell_script(script, path)
        self._output = subprocess.check_output(
            [self._shell_cmd, sh_script], shell=False,
            stderr=subprocess.STDOUT
        )
        return self._output


if __name__ == '__main__':
    p = r'../dumpscripts/inspect_getsource_class.py'
    c = CaptureOutputScript()
    output = c.run(p)
    print output
    print "Fine"

