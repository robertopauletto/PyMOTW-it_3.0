# argparse_custom_action.py

import argparse


class AzionePersonalizzata(argparse.Action):
    def __init__(self,
                 option_strings,
                 dest,
                 nargs=None,
                 const=None,
                 default=None,
                 type=None,
                 choices=None,
                 required=False,
                 help=None,
                 metavar=None):
        argparse.Action.__init__(self,
                                 option_strings=option_strings,
                                 dest=dest,
                                 nargs=nargs,
                                 const=const,
                                 default=default,
                                 type=type,
                                 choices=choices,
                                 required=required,
                                 help=help,
                                 metavar=metavar,
                                 )
        print('Inizializzazione di AzionePersonalizzata')
        for name, value in sorted(locals().items()):
            if name == 'self' or value is None:
                continue
            print('  {} = {!r}'.format(name, value))
        print()
        return

    def __call__(self, parser, namespace, values, option_string=None):
        print('Elaborazione di AzionePersonalizzata per {}'.format(self.dest))
        print('  parser = {}'.format(id(parser)))
        print('  values = {!r}'.format(values))
        print('  option_string = {!r}'.format(option_string))

        # Si esegue qualche arbitraria elaborazione dei valori in input
        if isinstance(values, list):
            values = [v.upper() for v in values]
        else:
            values = values.upper()
        # Si salvano i risultati nello spazio dei nomi utilizzando
        # la variabile di destinazione passata al costruttore
        setattr(namespace, self.dest, values)
        print()


parser = argparse.ArgumentParser()

parser.add_argument('-a', action=AzionePersonalizzata)
parser.add_argument('-m', nargs='*', action=AzionePersonalizzata)

results = parser.parse_args([
                            '-a', 'value', '-m',
                            'multi-valore', 'valore-posizionale'])
print(results)
