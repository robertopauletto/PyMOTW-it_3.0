#!/usr/binf/env python
# -*- coding: UTF-8 -*-


import itertools
import mimetools
import mimetypes
from cStringIO import StringIO
import urllib
import urllib2

class MultiPartForm(object):
    """Accumula i dati da usare quando si invia un form."""

    def __init__(self):
        self.form_fields = []
        self.files = []
        self.boundary = mimetools.choose_boundary()
        return
    
    def get_content_type(self):
        return 'multipart/form-data; boundary=%s' % self.boundary

    def add_field(self, name, value):
        """Aggiunge un semplice campi ai dati del form."""
        self.form_fields.append((name, value))
        return

    def add_file(self, fieldname, filename, fileHandle, mimetype=None):
        """Aggiunge un file da inviare."""
        body = fileHandle.read()
        if mimetype is None:
            mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        self.files.append((fieldname, filename, mimetype, body))
        return
    
    def __str__(self):
        """Ritorna una stringa che rappresenta i dati del form, compresi i file allegati."""
        # Costruisce una lista di liste, ognuna contenente righe ("lines") della
        # richiesta. Ogni parte è separata da una stringa di limite.
        # Una volta costruita la lista, si ritorna una stringa con ciascuna riga
        # separata da '\r\n'.  
        parts = []
        part_boundary = '--' + self.boundary
        
        # Aggiunge i campi del form
        parts.extend(
            [ part_boundary,
              'Content-Disposition: form-data; name="%s"' % name,
              '',
              value,
            ]
            for name, value in self.form_fields
            )
        
        # Aggiunge i file da inviare
        parts.extend(
            [ part_boundary,
              'Content-Disposition: file; name="%s"; filename="%s"' % \
                 (field_name, filename),
              'Content-Type: %s' % content_type,
              '',
              body,
            ]
            for field_name, filename, content_type, body in self.files
            )
        
        # Riunisce le liste ed aggiunge il marcatori di limite di chiusura,
        # poi ritorna i dati separati da CR/LF
        flattened = list(itertools.chain(*parts))
        flattened.append('--' + self.boundary + '--')
        flattened.append('')
        return '\r\n'.join(flattened)

if __name__ == '__main__':
    # Crea il form con semplici campi
    form = MultiPartForm()
    form.add_field('firstname', 'Doug')
    form.add_field('lastname', 'Hellmann')
    
    # Aggiunge un falso file
    form.add_file('biography', 'bio.txt', 
                  fileHandle=StringIO('Python developer and blogger.'))

    # Costruisce la richiesta
    request = urllib2.Request('http://localhost:8080/')
    request.add_header('User-agent', 'PyMOTW (http://www.doughellmann.com/PyMOTW/)')
    body = str(form)
    request.add_header('Content-type', form.get_content_type())
    request.add_header('Content-length', len(body))
    request.add_data(body)

    print
    print 'DATI IN USCITA     :'
    print request.get_data()

    print
    print 'RISPOSTA DEL SERVER:'
    print urllib2.urlopen(request).read()