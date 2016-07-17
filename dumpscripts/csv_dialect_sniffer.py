# csv_dialect_sniffer.py

import csv
from io import StringIO
import textwrap

csv.register_dialect('escaped',
                     escapechar='\\',
                     doublequote=False,
                     quoting=csv.QUOTE_NONE)
csv.register_dialect('singlequote',
                     quotechar="'",
                     quoting=csv.QUOTE_ALL)

# Genera dati campione per tutti i dialetti conosciuti
samples = []
for name in sorted(csv.list_dialects()):
    buffer = StringIO()
    dialect = csv.get_dialect(name)
    writer = csv.writer(buffer, dialect=dialect)
    writer.writerow(
        ('col1', 1, '10/01/2010',
         'Caratteri speciali " \' {} da elaborare'.format(
             dialect.delimiter))
    )
    samples.append((name, dialect, buffer.getvalue()))

# Indovina il dialetto per un dato campione, quindi utilizza i risultati per
# elaborare i dati.
sniffer = csv.Sniffer()
for name, expected, sample in samples:
    print('Dialetto: "{}"'.format(name))
    print('In: {}'.format(sample.rstrip()))
    dialect = sniffer.sniff(sample, delimiters=',\t')
    reader = csv.reader(StringIO(sample), dialect=dialect)
    print('Elaborati:\n  {}\n'.format(
          '\n  '.join(repr(r) for r in next(reader))))
