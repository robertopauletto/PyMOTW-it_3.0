# pyclbr_example.py
"""Sorgente di esempio per pyclbr
"""


class Base:
    """Questa è la classe base.
    """

    def method1(self):
        return


class Sub1(Base):
    """Questa è la prima sottoclasse.
    """


class Sub2(Base):
    """Questa è la seconda sottoclasse.
    """


class Mixin:
    """UNa classe mixin.
    """

    def method2(self):
        return


class MixinUser(Sub2, Mixin):
    """Sovrascrive i method1 e method2
    """

    def method1(self):
        return

    def method2(self):
        return

    def method3(self):
        return


def my_function():
    """Funzione a se stante.
    """
    return
