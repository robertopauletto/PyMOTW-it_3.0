#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sqlite3

db_filename = 'todo.db'

db_is_new = not os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)

if db_is_new:
    print 'Occorre creare lo schema'
else:
    print 'Il database esiste, si suppone che esista anche lo schema.'

conn.close()