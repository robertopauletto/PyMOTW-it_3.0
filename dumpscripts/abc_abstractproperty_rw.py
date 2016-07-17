#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# abc_abstractproperty_rw.py

import abc


class Base(abc.ABC):

    @property
    @abc.abstractmethod
    def value(self):
        return 'Non si dovrebbe mai arrivare qui'

    @value.setter
    @abc.abstractmethod
    def value(self, newvalue):
        return


class PartialImplementation(Base):

    @property
    def value(self):
        return 'Sola lettura'


class Implementation(Base):

    _value = 'Valore predefinito'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newvalue):
        self._value = newvalue


try:
    b = Base()
    print('Base.value:', b.value)
except Exception as err:
    print('ERRORE:', str(err))

try:
    p = PartialImplementation()
    print('PartialImplementation.value:', p.value)
    p.value = 'Alterazione'
    print('PartialImplementation.value:', p.value)
except Exception as err:
    print('ERRORE:', str(err))

i = Implementation()
print('Implementation.value:', i.value)

i.value = 'Nuovo valore'
print('Valore modificato:', i.value)
