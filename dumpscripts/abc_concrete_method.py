#!/usr/binf/env python
# -*- coding: UTF-8 -*-

# abc_concrete_method.py

import abc
import io


class ABCWithConcreteImplementation(abc.ABC):

    @abc.abstractmethod
    def retrieve_values(self, input):
        print('classe base per leggere dati')
        return input.read()


class ConcreteOverride(ABCWithConcreteImplementation):

    def retrieve_values(self, input):
        base_data = super(ConcreteOverride,
                          self).retrieve_values(input)
        print('sottoclasse che ordina dati')
        response = sorted(base_data.splitlines())
        return response


input = io.StringIO("""riga uno
riga due
riga tre
""")

reader = ConcreteOverride()
print(reader.retrieve_values(input))
print()
