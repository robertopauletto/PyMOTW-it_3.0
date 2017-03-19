# statistics_variance.py

from statistics import *
import subprocess


def get_line_lengths():
    cmd = 'wc -l ../[a-z]*/*.py'
    out = subprocess.check_output(
        cmd, shell=True).decode('utf-8')
    for line in out.splitlines():
        parts = line.split()
        if parts[1].strip().lower() == 'total':
            break
        nlines = int(parts[0].strip())
        if not nlines:
            continue  # skip empty files
        yield (nlines, parts[1].strip())


data = list(get_line_lengths())

lengths = [d[0] for d in data]
sample = lengths[::2]

print('Statistiche base:')
print('  conteggio: {:3d}'.format(len(lengths)))
print('  minimo   : {:6.2f}'.format(min(lengths)))
print('  massimo  : {:6.2f}'.format(max(lengths)))
print('  media    : {:6.2f}'.format(mean(lengths)))

print('\nVarianza nella popolazione:')
print('  deviazione standard: {:6.2f}'.format(pstdev(lengths)))
print('  varianza           : {:6.2f}'.format(pvariance(lengths)))

print('\nVarianza stimata per campione:')
print('  conteggio          : {:3d}'.format(len(sample)))
print('  deviazione standard: {:6.2f}'.format(stdev(sample)))
print('  varianza           : {:6.2f}'.format(variance(sample)))
