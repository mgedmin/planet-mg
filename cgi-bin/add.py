#!/usr/bin/python
import cgi


FORM = """\
<!DOCTYPE html>
<html>
  <head>
    <title>Add a subscription to Planet Mg</title>
    <link rel="stylesheet" href="planetmg.css">
  </head>
  <body>
    <h1>Add a subscription to Planet Mg</h1>
    <form method="get">
      <label for="url-field">Feed URL</label>
      <input type="text" name="url" id="url-field">
      <br>
      <input type="submit" value="Add">
    </form>
  </body>
</html>
"""


RESULT = """\
<!DOCTYPE html>
<html>
  <head>
    <title>Add a subscription to Planet Mg</title>
    <link rel="stylesheet" href="planetmg.css">
  </head>
  <body>
    <h1>Add a subscription to Planet Mg</h1>
    <p>
      This is a manual process: head over to Github and
      <a href="https://github.com/mgedmin/planet-mg/edit/master/config.ini">
      edit config.ini</a>, then add
    </p>
    <blockquote>
      <pre>[{url}]
name = {title}</pre>
    </blockquote>
  </body>
</html>
"""


def main():
    print "Content-Type: text/html; charset=UTF-8"
    print
    form = cgi.FieldStorage()
    if "url" not in form:
        print FORM
    else:
        url = form["url"].value
        title = '(name of blog)'
        print RESULT.format(url=cgi.escape(url), title=cgi.escape(title))


if __name__ == '__main__':
    main()


