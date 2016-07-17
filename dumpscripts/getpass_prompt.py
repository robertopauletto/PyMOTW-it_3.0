#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import getpass

p = getpass.getpass(prompt="Qual'è il tuo colore preferito? ")
if p.lower() == 'blu':
    print 'Corretto, puoi proseguire.'
else:
    print 'Auuuuugh!'