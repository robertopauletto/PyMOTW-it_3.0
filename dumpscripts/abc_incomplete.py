#!/usr/binf/env python
# -*- coding: UTF-8 -*-

# abc_incomplete.py

import abc
from abc_base import PluginBase


@PluginBase.register
class IncompleteImplementation(PluginBase):

    def save(self, output, data):
        return output.write(data)

if __name__ == '__main__':
    print('Sottoclasse:', issubclass(IncompleteImplementation,
                                  PluginBase))
    print('Istanza:', isinstance(IncompleteImplementation(),
                                  PluginBase))
