#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import asyncore
import os

class FileReader(asyncore.file_dispatcher):
    
    def writable(self):
        return False
    
    def handle_read(self):
        data = self.recv(256)
        print 'READ: (%d) "%s"' % (len(data), data)
        
    def handle_expt(self):
        # Ignora eventi che sembrano dati fuori banda
        pass
    
    def handle_close(self):
        self.close()

lorem_fd = os.open('lorem.txt', os.O_RDONLY)
reader = FileReader(lorem_fd)
asyncore.loop()