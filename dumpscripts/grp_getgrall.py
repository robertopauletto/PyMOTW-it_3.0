# grp_getgrall.py

import grp
import textwrap

# Carica tutti i dati dei gruppi, ordinati per nome
all_groups = grp.getgrall()
interesting_groups = {
    g.gr_name: g
    for g in all_groups
    if not g.gr_name.startswith('_')
}
print(len(interesting_groups.keys()))

# Trova la lunghezza massima di alcuni campi
name_length = max(len(k) for k in interesting_groups) + 1
gid_length = max(len(str(u.gr_gid))
                 for u in interesting_groups.values()) + 1

# Imposta la larghezza del campo dei membri per evitare il ritorno a campo
# nelle colonne della tabella
members_width = 19

# Stampa le intestazioni del report
fmt = ' '.join(['{:<{name_length}}',
                '{:{gid_length}}',
                '{:<{members_width}}',
                ])
print(fmt.format('Nome',
                 'GID',
                 'Membri',
                 name_length=name_length,
                 gid_length=gid_length,
                 members_width=members_width))
print('-' * name_length,
      '-' * gid_length,
      '-' * members_width)

# Stampa i dati
prefix = ' ' * (name_length + gid_length + 2)
for name, g in sorted(interesting_groups.items()):
    # Formatta i membri in modo che partano nella colonna sulla stessa riga ma
    # li racchiude come necessario con una indentazione sufficiente per
    # inserire le righe seguenti alla stessa altezza nella colonna membri
    # I due prefissi di indentazione devono essere uguali per calcolare
    # propriamente l'indentazione ma il primo non dovrebbe essere stampato,
    # quindi viene eliminato.
    members = textwrap.fill(
        ', '.join(g.gr_mem),
        initial_indent=prefix,
        subsequent_indent=prefix,
        width=members_width + len(prefix),
    ).strip()
    print(fmt.format(g.gr_name,
                     g.gr_gid,
                     members,
                     name_length=name_length,
                     gid_length=gid_length,
                     members_width=members_width))
