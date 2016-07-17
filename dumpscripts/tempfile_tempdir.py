import tempfile

tempfile.tempdir = '/Ho/cambiato/questo/percorso'
print 'gettempdir():', tempfile.gettempdir()
