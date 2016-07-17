#!/usr/binf/env python
# -*- coding: UTF-8 -*-


import mimetypes
import os
import tempfile
import urllib
import urllib2

class NFSFile(file):
    def __init__(self, tempdir, filename):
        self.tempdir = tempdir
        file.__init__(self, filename, 'rb')
    def close(self):
        print
        print 'NFSFile:'
        print '  sto smontando %s' % self.tempdir
        print '  quando %s è chiuso' % os.path.basename(self.name)
        return file.close(self)

class FauxNFSHandler(urllib2.BaseHandler):
    
    def __init__(self, tempdir):
        self.tempdir = tempdir
    
    def nfs_open(self, req):
        url = req.get_selector()
        directory_name, file_name = os.path.split(url)
        server_name = req.get_host()
        print
        print 'FauxNFSHandler simula il mount:'
        print '  Percorso remoto: %s' % directory_name
        print '  Server         : %s' % server_name
        print '  Percorso locale: %s' % tempdir
        print '  Nome file      : %s' % file_name
        local_file = os.path.join(tempdir, file_name)
        fp = NFSFile(tempdir, local_file)
        content_type = mimetypes.guess_type(file_name)[0] or 'application/octet-stream'
        stats = os.stat(local_file)
        size = stats.st_size
        headers = { 'Content-type': content_type,
                    'Content-length': size,
                  }
        return urllib.addinfourl(fp, headers, req.get_full_url())

if __name__ == '__main__':
    tempdir = tempfile.mkdtemp()
    try:
        # Popola il file temporaneo per la simulazione
        with open(os.path.join(tempdir, 'file.txt'), 'wt') as f:
            f.write('Contenuto di file.txt')
        
        # Costruisce un oggetto per l'apertura con l'handler NFS
        # e lo registra come predifinito.
        opener = urllib2.build_opener(FauxNFSHandler(tempdir))
        urllib2.install_opener(opener)

        # Apre il file tramite un URL
        response = urllib2.urlopen('nfs://server_remoto/percorso/a/file.txt')
        print
        print 'LEGGE CONTENUTO:', response.read()
        print 'URL          :', response.geturl()
        print 'HEADERS:'
        for name, value in sorted(response.info().items()):
            print '  %-15s = %s' % (name, value)
        response.close()
    finally:
        os.remove(os.path.join(tempdir, 'file.txt'))
        os.removedirs(tempdir)