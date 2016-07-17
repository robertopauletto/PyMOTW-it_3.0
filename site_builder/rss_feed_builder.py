#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""Crea il file xml che rappresenta un feed rss
"""

from rss2feed import RSS2Feed
import datetime

class FeedItem(object):
    """Rappresenta un elemento di un feed"""
    def __init__(self, title, lnk, descr='', date=datetime.datetime.utcnow(), guid=None):
        """(str, str [,str] [,datetime] [,guid] )
        
        Istanzia i campi di un feed
        """
        self._title = title
        self._lnk = lnk
        self._descr = descr
        self._dt = date
        self._guid = guid
        

class Feed(object):
    """Rappresenta un file rss """
    def __init__(self, title, link, description=''):
        """(str, str [,str])
        
        Istanzia titolo, indirizzo e descrizione del feed
        """
        self._title = title
        self._link = link
        self._descr = description
        self._items = []
        
    def set_item(self, feed_item):
        """`FeedItem`
        
        Aggiunge un elemento al feed
        """
        assert isinstance(feed_item, FeedItem)
        self._items.append(feed_item)
    
    def get_feed(self, pretty=True):
        """Ritorna la rappresentazione xml del feed"""
        if not self._items:
            raise AttributeError("Almeno un elemento deve essere presente")
        feed = RSS2Feed(self._title, self._link, self._descr)
        for item in self._items:
            feed.append_item(
                title=item._title,
                link=item._lnk,
                description=item._descr, 
                pub_date=item._dt,
                guid=item._guid
            )
        return feed.get_xml(pretty)
    
    