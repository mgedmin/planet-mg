#!/usr/bin/python
"""Fix the Sandra and Woo feed.

The RSS source looks roughly like this::

    <item>
      <title>[NNNN] Title</title>
      <link>http://feedproxy.google.com/~r/sandraandwoo/.../</link>
      <guid isPermaLink="false">http://www.sandraandwoo.com/YYYY/MM/DD/NNNN-title/</guid>
      <description>
        <![CDATA[
          <p>
            <a href="http://www.sandraandwoo.com/YYYY/MM/DD/NNNN-title/">
              <img src="http://www.sandraandwoo.com/comics_rss/YYYY-MM-DD-NNNN-title.png"
                   border="0" alt="[NNNN] Title" title="[NNNN] Title" />
            </a>
          </p>
          Text text text [&#8230;]]]>
      </description>
      <p>
        <a href="http://www.sandraandwoo.com/YYYY/MM/DD/NNNN-title/">
          <img src="http://www.sandraandwoo.com/comics_rss/YYYY-MM-DD-NNNN-title.png"
               border="0" alt="[NNNN] Title" title="[NNNN] Title"/>
        </a>
      </p>
      <content:encoded>
        <![CDATA[
          <p>Text text text...</p>
      </content:encoded>
    </item>

Planet mangles it into the following ATOM::

    <entry xmlns=".../Atom">
      <id>http://www.sandraandwoo.com/YYYY/MM/DD/NNNN-title/</id>
      <summary type="xhtml">
        <div xmlns="http://www.w3.org/1999/xhtml">
          <p>
            <a target="_blank" href="http://www.sandraandwoo.com/YYYY/MM/DD/NNNN-title/">
              <img alt="[NNNN] Title" border="0"
                   src="http://www.sandraandwoo.com/comics_rss/YYYY-MM-DD-NNNN-title.png"
                   title="[NNNN] Title"/>
            </a>
          </p>
          Text text text ... [&#x2026;]
        </div>
      </summary>
      <content type="xhtml">
        <div xmlns="http://www.w3.org/1999/xhtml">
          <p>Text text text...</p>
        </div>
      </content>
    </entry>

"""
import sys
import copy
import lxml.etree

doc = lxml.etree.parse(sys.stdin)

atom = "http://www.w3.org/2005/Atom"
xhtml = 'http://www.w3.org/1999/xhtml'
nsmap = dict(xhtml=xhtml, atom=atom)

# This is the same as filters/fixchaoslife.py, unify!
comiclinks = doc.xpath('//atom:summary/xhtml:div/xhtml:p[xhtml:a[xhtml:img]]',
                       namespaces=nsmap)
if comiclinks:
    content_div = doc.xpath('//atom:content/xhtml:div', namespaces=nsmap)[0]
    for el in reversed(comiclinks):
        el = copy.deepcopy(el)
        el.tail = ''
        content_div.insert(0, el)

print(lxml.etree.tostring(doc))
