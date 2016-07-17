import tempfile

f = tempfile.TemporaryFile(mode='w+t')
try:
    f.writelines(['primo\n', 'secondo\n'])
    f.seek(0)

    for line in f:
        print line.rstrip()
finally:
    f.close()