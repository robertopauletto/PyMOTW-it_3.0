# urllib_request_nfs_handler.py

import io
import mimetypes
import os
import tempfile
from urllib import request
from urllib import response


class NFSFile:

    def __init__(self, tempdir, filename):
        self.tempdir = tempdir
        self.filename = filename
        with open(os.path.join(tempdir, filename), 'rb') as f:
            self.buffer = io.BytesIO(f.read())

    def read(self, *args):
        return self.buffer.read(*args)

    def readline(self, *args):
        return self.buffer.readline(*args)

    def close(self):
        print('\nNFSFile:')
        print('  sto smontando {}'.format(
            os.path.basename(self.tempdir)))
        print('  quando {} è chiuso'.format(
            os.path.basename(self.filename)))


class FauxNFSHandler(request.BaseHandler):

    def __init__(self, tempdir):
        self.tempdir = tempdir
        super().__init__()

    def nfs_open(self, req):
        url = req.full_url
        directory_name, file_name = os.path.split(url)
        server_name = req.host
        print('Simulazione montaggio FauxNFSHandler:')
        print('  Percorso remoto : {}'.format(directory_name))
        print('  Server          : {}'.format(server_name))
        print('  Percorso locale : {}'.format(
            os.path.basename(tempdir)))
        print('  Nome file       : {}'.format(file_name))
        local_file = os.path.join(tempdir, file_name)
        fp = NFSFile(tempdir, file_name)
        content_type = (
            mimetypes.guess_type(file_name)[0] or
            'application/octet-stream'
        )
        stats = os.stat(local_file)
        size = stats.st_size
        headers = {
            'Content-type': content_type,
            'Content-length': size,
        }
        return response.addinfourl(fp, headers,
                                   req.get_full_url())


if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as tempdir:
        # Popola il file temporaneo per la simulazione
        filename = os.path.join(tempdir, 'file.txt')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('Contents of file.txt')

        # Costruisce un opener con il nostro handler NFS
        # e lo registra come predefinito.
        opener = request.build_opener(FauxNFSHandler(tempdir))
        request.install_opener(opener)

        # Apre il file tramite un URL.
        resp = request.urlopen(
            'nfs://remote_server/path/to/the/file.txt'
        )
        print()
        print('CONTENUTO LETTO:', resp.read())
        print('URL            :', resp.geturl())
        print('INTESTAZIONI   :')
        for name, value in sorted(resp.info().items()):
            print('  {:<15} = {}'.format(name, value))
        resp.close()
