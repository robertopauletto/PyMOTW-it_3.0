import argparse

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(help='comandi')

# Un comando di elenco
list_parser = subparsers.add_parser('elenca', help='Elenco contenuto')
list_parser.add_argument('nomedir', action='store', help='Directory da elencare')

# Un comando di creazione
create_parser = subparsers.add_parser('crea', help='Crea una directory')
create_parser.add_argument('nomedir', action='store', help='Nuova directory da creare')
create_parser.add_argument('--sola-lettura', default=False, action='store_true',
                           help='Imposta i permessi per evitare di scrivere alla directory',
                           )

# Un comando di eliminazione
delete_parser = subparsers.add_parser('elimina', help='Elimina una directory')
delete_parser.add_argument('nomedir', action='store', help='La directory da eliminare')
delete_parser.add_argument('--ricorsiva', '-r', default=False, action='store_true',
                           help='Elimina anche il contenuto della directory',
                           )

print parser.parse_args()