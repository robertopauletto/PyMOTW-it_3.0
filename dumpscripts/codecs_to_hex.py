import binascii

def to_hex(t, nbytes):
    "Formattazione del testo t come sequenza valori nbyte long separati da spazi."
    chars_per_item = nbytes * 2
    hex_version = binascii.hexlify(t)
    num_chunks = len(hex_version) / chars_per_item
    def chunkify():
        for start in xrange(0, len(hex_version), chars_per_item):
            yield hex_version[start:start + chars_per_item]
    return ' '.join(chunkify())

if __name__ == '__main__':
    print to_hex('abcdef', 1)
    print to_hex('abcdef', 2)