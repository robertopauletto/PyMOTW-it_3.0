import tempfile

temp = tempfile.NamedTemporaryFile(suffix='_suffisso', 
                                   prefix='prefisso_', 
                                   dir='/tmp',
                                   )
try:
    print 'temp:', temp
    print 'temp.name:', temp.name
finally:
    temp.close()
