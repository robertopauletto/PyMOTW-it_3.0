# codecs_invertcaps_register.py

import codecs

from codecs_invertcaps_charmap import encoding_map, decoding_map


class InvertCapsCodec(codecs.Codec):
    "Stateless encoder/decoder"

    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_map)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_map)


class InvertCapsIncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        data, nbytes = codecs.charmap_encode(input,
                                             self.errors,
                                             encoding_map)
        return data


class InvertCapsIncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        data, nbytes = codecs.charmap_decode(input,
                                             self.errors,
                                             decoding_map)
        return data


class InvertCapsStreamReader(InvertCapsCodec,
                             codecs.StreamReader):
    pass


class InvertCapsStreamWriter(InvertCapsCodec,
                             codecs.StreamWriter):
    pass


def find_invertcaps(encoding):
    """Ritorna il codec per 'invertcaps'.
    """
    if encoding == 'invertcaps':
        return codecs.CodecInfo(
            name='invertcaps',
            encode=InvertCapsCodec().encode,
            decode=InvertCapsCodec().decode,
            incrementalencoder=InvertCapsIncrementalEncoder,
            incrementaldecoder=InvertCapsIncrementalDecoder,
            streamreader=InvertCapsStreamReader,
            streamwriter=InvertCapsStreamWriter,
        )
    return None


codecs.register(find_invertcaps)

if __name__ == '__main__':

    # Stateless encoder/decoder
    encoder = codecs.getencoder('invertcaps')
    text = 'abcDEF'
    encoded_text, consumed = encoder(text)
    print('Codificati "{}" in "{}", consumando {} caratteri'.format(
        text, encoded_text, consumed))

    # Scrittore di flusso
    import io
    buffer = io.BytesIO()
    writer = codecs.getwriter('invertcaps')(buffer)
    print('StreamWriter per il buffer io: ')
    print('  scrittura di "abcDEF"')
    writer.write('abcDEF')
    print('  contenuto del buffer: ', buffer.getvalue())

    # Incremental decoder
    decoder_factory = codecs.getincrementaldecoder('invertcaps')
    decoder = decoder_factory()
    decoded_text_parts = []
    for c in encoded_text:
        decoded_text_parts.append(
            decoder.decode(bytes([c]), final=False)
        )
    decoded_text_parts.append(decoder.decode(b'', final=True))
    decoded_text = ''.join(decoded_text_parts)
    print('IncrementalDecoder convertito {!r} a {!r}'.format(
        encoded_text, decoded_text))
