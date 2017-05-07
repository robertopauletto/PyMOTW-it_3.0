# urllib_request_upload_files.py

import io
import mimetypes
from urllib import request
import uuid


class MultiPartForm:
    """Raccoglie i dati da usare quando si invia un form."""

    def __init__(self):
        self.form_fields = []
        self.files = []
        # Usa una grande string di byte casuali per separere le
        # parti dei dati MIME.
        self.boundary = uuid.uuid4().hex.encode('utf-8')
        return

    def get_content_type(self):
        return 'multipart/form-data; boundary={}'.format(
            self.boundary.decode('utf-8'))

    def add_field(self, name, value):
        """Aggiunge un campo semplice ai dati del form."""
        self.form_fields.append((name, value))

    def add_file(self, fieldname, filename, fileHandle,
                 mimetype=None):
        """Aggiunte un file da inviare."""
        body = fileHandle.read()
        if mimetype is None:
            mimetype = (
                mimetypes.guess_type(filename)[0] or
                'application/octet-stream'
            )
        self.files.append((fieldname, filename, mimetype, body))
        return

    @staticmethod
    def _form_data(name):
        return ('Content-Disposition: form-data; '
                'name="{}"\r\n').format(name).encode('utf-8')

    @staticmethod
    def _attached_file(name, filename):
        return ('Content-Disposition: file; '
                'name="{}"; filename="{}"\r\n').format(
                    name, filename).encode('utf-8')

    @staticmethod
    def _content_type(ct):
        return 'Content-Type: {}\r\n'.format(ct).encode('utf-8')

    def __bytes__(self):
        """Rttorna una stringa di byte che rappresentano i dati del form,
        compreso i file allegati
        """
        buffer = io.BytesIO()
        boundary = b'--' + self.boundary + b'\r\n'

        # Aggiunge i campi del form
        for name, value in self.form_fields:
            buffer.write(boundary)
            buffer.write(self._form_data(name))
            buffer.write(b'\r\n')
            buffer.write(value.encode('utf-8'))
            buffer.write(b'\r\n')

        # Aggiunge i fiel da inviare
        for f_name, filename, f_content_type, body in self.files:
            buffer.write(boundary)
            buffer.write(self._attached_file(f_name, filename))
            buffer.write(self._content_type(f_content_type))
            buffer.write(b'\r\n')
            buffer.write(body)
            buffer.write(b'\r\n')

        buffer.write(b'--' + self.boundary + b'--\r\n')
        return buffer.getvalue()


if __name__ == '__main__':
    # Creat il form con campi semplici
    form = MultiPartForm()
    form.add_field('firstname', 'Doug')
    form.add_field('lastname', 'Hellmann')

    # Aggiunge un file fasullo
    form.add_file(
        'biography', 'bio.txt',
        fileHandle=io.BytesIO(b'Python developer and blogger.'))

    # Costruisce la richiesta, compresa la stringa di byte
    # per i dati da inviare.
    data = bytes(form)
    r = request.Request('http://localhost:8080/', data=data)
    r.add_header(
        'User-agent',
        'PyMOTW (https://pymotw.com/)',
    )
    r.add_header('Content-type', form.get_content_type())
    r.add_header('Content-length', len(data))

    print()
    print('DATI IN USCITA:')
    for name, value in r.header_items():
        print('{}: {}'.format(name, value))
    print()
    print(r.data.decode('utf-8'))

    print()
    print('RISPOSTA DEL SERVER:')
    print(request.urlopen(r).read().decode('utf-8'))
