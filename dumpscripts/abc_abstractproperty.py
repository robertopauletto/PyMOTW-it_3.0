#!/usr/binf/env python
# -*- coding: UTF-8 -*-

# abc_abstractproperty.py

import abc


class Base(abc.ABC):

    @property
    @abc.abstractmethod
    def value(self):
        return 'Non si dovrebbe mai arrivare qui'

    @property
    @abc.abstractmethod
    def constant(self):
        return 'Non si dovrebbe mai arrivare qui'


class Implementation(Base):

    @property
    def value(self):
        return 'proprietà concreta'

    constant = 'impostata da un attributo di classe'


try:
    b = Base()
    print('Base.value:', b.value)
except Exception as err:
    print('ERRORE:', str(err))

i = Implementation()
print('Implementation.value   :', i.value)
print('Implementation.constant:', i.constant)
