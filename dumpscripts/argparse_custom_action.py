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
        print
        print 'Inizializzazione di AzionePersonalizzata'
        for name,value in sorted(locals().items()):
            if name == 'self' or value is None:
                continue
            print '  %s = %r' % (name, value)
        return

    def __call__(self, parser, namespace, values, option_string=None):
        print
        print 'Elaborazione di AzionePersonalizzata per "%s"' % self.dest
        print '  parser = %s' % id(parser)
        print '  values = %r' % values
        print '  option_string = %r' % option_string
        
        # Do some arbitrary processing of the input values
        # Si esegue qualche arbitraria elaborazione dei valori in input
        if isinstance(values, list):
            values = [ v.upper() for v in values ]
        else:
            values = values.upper()
        # Si salvano i risultati nello spazio dei nomi utilizzando
        # la variabile di destinazione passata al costruttore
        setattr(namespace, self.dest, values)

parser = argparse.ArgumentParser()

parser.add_argument('-a', action=AzionePersonalizzata)
parser.add_argument('-m', nargs='*', action=AzionePersonalizzata)
parser.add_argument('positional', action=AzionePersonalizzata)

results = parser.parse_args(['-a', 'value', '-m' 'multi-valore', 'valore-posizionale'])
print
print results