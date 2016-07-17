# abc_class_static.py

import abc


class Base(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def factory(cls, *args):
        return cls()

    @staticmethod
    @abc.abstractmethod
    def const_behavior():
        return 'Non si dovrebbe mai arrivare qui'


class Implementation(Base):

    def do_something(self):
        pass

    @classmethod
    def factory(cls, *args):
        obj = cls(*args)
        obj.do_something()
        return obj

    @staticmethod
    def const_behavior():
        return 'Il comportamento statico differisce'


try:
    o = Base.factory()
    print('Base.value:', o.const_behavior())
except Exception as err:
    print('ERRORE:', str(err))

i = Implementation.factory()
print('Implementation.const_behavior :', i.const_behavior())
