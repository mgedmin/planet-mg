#!/usr/bin/python
"""Inline the Girl Genius Online comic image.

The RSS source looks roughly like this::

    <item>
      <title>...</title>
      <link>http://www.girlgeniusonline.com/comic.php?date=YYYYMMDD</link>
      <description>The Girl Genius comic for Weekday, Month DD, YYYY has been
      posted.</description>
    </item>

Planet mangles it into the following ATOM::

    <entry xmlns=".../Atom">
      <id>http://www.girlgeniusonline.com/comic.php?date=YYYYMMDD</id>
      <link href="http://www.girlgeniusonline.com/comic.php?date=YYYYMMDD"
            type="text/html"/>
      <summary>The Girl Genius comic for Weekday, Month DD, YYYY has been
      posted.</summary>
    </entry>

The comics are found at URLs like

    http://www.girlgeniusonline.com/ggmain/strips/ggmainYYYYMMDDa.jpg

Sometimes the comics are double-pages.  You should view them on the main
website.
"""
import sys
import lxml.etree

doc = lxml.etree.parse(sys.stdin)

img_link_pattern = 'http://www.girlgeniusonline.com/ggmain/strips/ggmain%sa.jpg'

atom = "http://www.w3.org/2005/Atom"
xhtml = 'http://www.w3.org/1999/xhtml'
nsmap = dict(xhtml=xhtml, atom=atom)

entry = doc.xpath('//atom:entry', namespaces=nsmap)
link = doc.xpath('//atom:link[@type="text/html"]', namespaces=nsmap)
if link:
    entry = entry[0]
    link = link[0].get('href')
    date = link.rpartition('=')[-1]
    img_link = img_link_pattern % date
    content = lxml.etree.SubElement(entry, '{%s}content' % atom,
                                    {'type': 'xhtml'})
    div = lxml.etree.SubElement(content, '{%s}div' % xhtml)
    a = lxml.etree.SubElement(div, '{%s}a' % xhtml, {'href': link})
    img = lxml.etree.SubElement(a, '{%s}img' % xhtml,
                                {'src': img_link, 'alt': 'Comic for %s' % date})

print(lxml.etree.tostring(doc))
