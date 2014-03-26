#!/usr/bin/python
"""Add missing <author> to LiveJournal feeds

Planet's ATOM looks like this:

    <entry xmlns=".../Atom">
      ...
      <source>
        <author>
          <name>lj_username</name>
        </author>
        ...
      </content>
    </entry>

and we want to duplicate the <author> element one level up so Feedly will
show it to me.
"""
import sys
import copy
import lxml.etree

doc = lxml.etree.parse(sys.stdin)

atom = "http://www.w3.org/2005/Atom"
xhtml = 'http://www.w3.org/1999/xhtml'
nsmap = dict(xhtml=xhtml, atom=atom)

entry = doc.xpath('/atom:entry', namespaces=nsmap)[0]
if not entry.xpath('./atom:author', namespaces=nsmap):
    author = entry.xpath('./atom:source/atom:author', namespaces=nsmap)
    if author:
        entry.append(copy.deepcopy(author[0]))

print(lxml.etree.tostring(doc))
