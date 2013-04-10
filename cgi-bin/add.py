#!/usr/bin/python
import cgi
import os
import urllib
from contextlib import closing
from xml.etree import cElementTree as ET


here = os.path.dirname(__file__)
root = os.path.normpath(os.path.join(here, os.pardir))


DEFAULT_SIDEBAR = """\
    <div class="sidebar">
      <img class="logo" src="images/logo.png" width="136" height="136"
           alt="a picture of me">
    </div>
"""


def snarf_sidebar(default=DEFAULT_SIDEBAR):
    try:
        with open(os.path.join(root, 'output', 'index.html')) as f:
            body = f.read()
    except IOError:
        return default
    marker, sidebar = body.rpartition('<div class="sidebar">')[-2:]
    if not sidebar:
        return default
    return marker + sidebar.partition('</body>')[0]


LAYOUT = """
<!DOCTYPE html>
<html>
  <head>
    <title>Add a subscription to Planet Mg</title>
    <link rel="stylesheet" href="planet.css">
  </head>
  <body class="add-feed">
    <h1>Planet Mg</h1>
    <h2>Add a subscription</h2>
{{body}}
{sidebar}
  </body>
</html>
""".format(sidebar=snarf_sidebar())


FORM = LAYOUT.format(body="""\
    <form class="add-feed" method="get">
      <label for="url-field">Feed URL</label>
      <input type="text" name="url" id="url-field">
      <input type="submit" value="Add">
    </form>
""")


RESULT = LAYOUT.format(body="""\
    <p>
      This is a manual process: head over to Github and
      <a href="https://github.com/mgedmin/planet-mg/edit/master/config.ini">
      edit config.ini</a>, then add
    </p>
    <blockquote class="example">
      <pre>[{url}]
# name = {title}</pre>
    </blockquote>
    <p>
      Raw source of the feed:
    </p>
    <blockquote class="feed-source">
      <pre>{source}</pre>
    </blockquote>
""")


def fetch(url):
    with closing(urllib.urlopen(url)) as f:
        return f.read()


def feed_title(source):
    tree = ET.fromstring(source)
    rss_title = tree.find('channel/title')
    if rss_title is not None:
        return rss_title.text
    return None


def main():
    print "Content-Type: text/html; charset=UTF-8"
    print
    form = cgi.FieldStorage()
    if "url" not in form:
        print FORM
    else:
        url = form["url"].value
        source = fetch(url)
        title = feed_title(source) or '(name of blog)'
        print RESULT.format(url=cgi.escape(url), title=cgi.escape(title),
                            source=cgi.escape(source))


if __name__ == '__main__':
    main()


