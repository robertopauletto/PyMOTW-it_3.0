"""Provides the RSS2Feed class."""

from calendar import timegm
from email.utils import formatdate
from xml.dom.minidom import Document

class RSS2Feed(object):
    """An RSS 2.0 feed."""

    class FeedError(Exception):
        """Error encountered while producing a feed."""

    def __init__(self, title, link, description, pub_date=None, bld_date=None):
        """Initialize the feed with the specified attributes.

        :param title: brief title for the feed
        :param link: URL for the page containing the syndicated content
        :param description: longer description for the feed
        :param pub_date: last publication date for the feed (optional)
        :param bld_date: last modified-date for the feed (optional)
        """
        self._document = Document()
        rss_element = self._document.createElement('rss')
        rss_element.setAttribute('version', '2.0')
        self._document.appendChild(rss_element)
        self._channel = self._document.createElement('channel')
        rss_element.appendChild(self._channel)
        self._channel.appendChild(self._create_text_element('title', title))
        self._channel.appendChild(self._create_text_element('link', link))
        self._channel.appendChild(
            self._create_text_element('description', description)
        )
        if not pub_date is None:
            self._set_date('pubDate', pub_date)
        if not bld_date is None:
            self._set_date('lastBuildDate', bld_date)
            
            
    def _set_date(self, tag_name, date):
        """(str, datetime.datetime)
        
        Sets `tag_name`  with `date`
        """
        try:
            timestamp = int(date)
        except TypeError:
            timestamp = timegm(date.utctimetuple())
        element.appendChild(
            self._create_text_element(
                tag_name, formatdate(timestamp)
            )
        )
        

    def _create_text_element(self, type_, text):
        """Create a text element and return it."""
        element = self._document.createElement(type_)
        element.appendChild(self._document.createTextNode(text))
        return element

    def append_item(self, title=None, link=None, description=None,
                    pub_date=None, guid=None):
        """Append the specified item to the feed.

        :param title: brief title for the item
        :param link: URL for the page for the item
        :param description: longer drescription for the item
        :param guid: globally unique identifier. It's a string that uniquely
        identifies the item. 
        """
        # Either title or description *must* be present
        if title is None and description is None:
            raise self.FeedError("Either title or description must be provided.")
        element = self._document.createElement('item')
        if not title is None:
            element.appendChild(self._create_text_element('title', title))
        if not link is None:
            element.appendChild(self._create_text_element('link', link))
        if not description is None:
            element.appendChild(
                self._create_text_element('description', description)
            )
        if not pub_date is None:
            try:
                timestamp = int(pub_date)
            except TypeError:
                timestamp = timegm(pub_date.utctimetuple())
            element.appendChild(
                self._create_text_element('pubDate', formatdate(timestamp))
            )
        if not guid is None:
            element.appendChild(self._create_text_element('guid', guid))
        self._channel.appendChild(element)

    def get_xml(self, pretty_print=True):
        """Return the XML for the feed.

        :pretty_print: if `True` returns a pretty print representation 
        :returns: XML representation of the RSS feed
        """
        return self._document.toxml() \
               if not pretty_print else self._document.toprettyxml()

