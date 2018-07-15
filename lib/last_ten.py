#!/usr/bin/env python
# -*- coding: utf-8 -*-
# last_ten.py

import datetime
import re


__doc__ = """Rappresenta gli ultimi 10 moduli tradotti/aggiornati"""
__version__ = "0.1"
__changelog__ = """
2018-07-15: prima stesura
"""


class LastTen(object):
    """Rappresentazione degli ultimi 10 moduli tradotti/aggiornati"""
    date_fmt = '%d.%M.%Y'

    def __init__(self, last_upd, name, descr):
        """

        :param last_upd: Ultimo aggiornamento - pattern formato LastTen.date_fmt
        :param name: nome modulo
        :param descr: descrizione
        """
        self._last_upd = datetime.datetime.strptime(last_upd, LastTen.date_fmt)
        self.name = name.lower().strip()
        self.descr = descr.strip()

    @property
    def last_upd(self):
        return self._last_upd.strftime(LastTen.date_fmt)

    @property
    def title(self):
        return "{} - {}".format(self.name, self.descr)


    def __str__(self):
        return "{}: {} - {}".format(self.last_upd, self.name, self.descr)


def LastTen_factory(rows):
    """Ritorna una lista di oggetti :class Lastten:

    Prerequisito: la riga è nel formato dd.mm.aaaa\tnome - descrizione"""
    last_ten = list()
    for row in rows:
        dt, _tmp = re.split('\s+', row, 1)
        name, descr = _tmp.split('-', 1)
        last_ten.append(LastTen(dt, name, descr))
    return last_ten


if __name__ == '__main__':
    fn = r'../cronologia.txt'
    rows = [row.strip() for row in open(fn) if row]
    last_ten = LastTen_factory(rows[-10:] if len(rows) >= 10 else rows)
    print('\n'.join(str(item) for item in last_ten))
