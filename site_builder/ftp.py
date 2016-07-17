#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""Ftp Library
"""
import sys
import os.path
from ftplib import FTP

ftp = FTP()

class FTPClient(object):
    """"""
    log = []
    def __init__(self):
        pass
    
    def connetti(self, host, user, pw, porta=21):
        try:
            ftp.connect(host, porta)
            ftp.login(user, pw)
        except Exception as e:
            print(e)
            sys.exit(1)
            
    def crea_dir(self, nome_dir):
        try:
            ftp.mkd(nome_dir)
        except Exception as e:
            print(e)
            sys.exit(1)

    def vai_a(self, nome_dir):
        try:
            ftp.cwd(nome_dir)
        except Exception as e:
            print(e)
            sys.exit(1)

    def invia(self, elenco_file):
        try:
            for f in elenco_file:
                self._invia(f)
        except Exception as e:
            print(e)
            sys.exit(1)
    
           
    
    file_binari = ['.pdf', '.jpg', '.gif', '.png']
    file_testo = ['.html', '.htm', '.xml', '.txt']
    def _invia(self, nome_file):
        root, ext = os.path.splitext(nome_file)
        if ext.lower() in file_binari:
            with open(nome_file, mode='rb') as fh:
                ftp.storbinary('STOR %s' % os.path.basename(nome_file))
        else:
            with open(nome_file, mode='rb') as fh:
                ftp.storlines('STOR %s' % os.path.basename(nome_file))
            
            
    def __del__(self):
        ftp.close()
        
if __name__ == '__main__':
    l = [riga.strip() for riga in open(r'/home/robby/.ftp_x10host')]
    conn = FTPClient()
    conn.connetti(l[0], l[1], l[2],)
    conn.invia(r'/home/robby/test_ftp.txt')
    conn.__del__()
    