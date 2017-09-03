#!/usr/bin/env python
# -*- coding: utf-8 -*-
# notifier

import notify2

__doc__ = """nuovo script"""
__version__ = "0.1"
__changelog__ = """

"""

ICON = r'static/img/pymotw.png'
APP = 'PyMOTW-it 3'


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class Notifier(Singleton):

    def __init__(self, appname, icon, urgency=None, timeout=None):
        self._appname = appname
        self._icon = icon
        self._urgency = urgency if urgency else notify2.URGENCY_NORMAL
        self._timeout = timeout if timeout else 1000
        notify2.init(self._appname)
        self._nobj = notify2.Notification(appname, icon=ICON)

    def notify(self, message):
        self._nobj.update(APP, message)
        self._nobj.show()


def get_notifier():
    notify2.init(APP)
    nobj = notify2.Notification(APP,icon=ICON)
    nobj.set_urgency(notify2.URGENCY_NORMAL)
    nobj.set_timeout(1000)
    return nobj


def notify(nobj, message):
    nobj.update(APP, message)
    nobj.show()


if __name__ == '__main__':
    nobj = get_notifier()
    notify(nobj, "Una notifica!!!")
