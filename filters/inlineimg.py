#!/usr/bin/python
import sys
import re
import lxml.etree

doc = lxml.etree.parse(sys.stdin)

xhtml = 'http://www.w3.org/1999/xhtml'
nsmap = dict(xhtml=xhtml)

urlmap = {
    r'http://www.kevinandkell.com/(\d\d\d\d)/kk(\d\d\d\d).html':
        r'http://www.kevinandkell.com/\1/strips/kk\1\2.jpg',
}

links = doc.xpath("//xhtml:a[@href]", namespaces=nsmap)
for link in links:
    href = link.get('href')
    for pattern, replacement in urlmap.items():
        if re.match(pattern, href):
            href = re.sub(pattern, replacement, href)
            parent = link.getparent()
            br = lxml.etree.SubElement(parent, 'br')
            img = lxml.etree.SubElement(parent, 'img', attrib=dict(src=href))

print(lxml.etree.tostring(doc))
