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
