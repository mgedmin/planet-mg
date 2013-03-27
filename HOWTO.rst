How do I ...?
=============


Where's the documentation of the config file?
---------------------------------------------

Very easily found: http://intertwingly.net/code/venus/docs/index.html


Can I define a feed in sources.xml then override something in config.ini?
-------------------------------------------------------------------------

Yes.  Just add ::

   [http://...feed-url...]
   ...overrides...

to ``config.ini``.  When testing, don't forget to remove the cached *source*
(see next question)!


How do I test feed settings changes in config.ini?
--------------------------------------------------

Do ::

    rm cache/sources/...feed...*
    bin/planet -n

This is necessary because many of the settings take effect during input
processing, which happens only when you fetch new content for the feed.


How do I fix a feed that keeps floating its entries to the top?
---------------------------------------------------------------

Edit ``config.ini`` and add ::

    [http://...feed-url...]
    ignore_in_feed = updated


How do I add a missing link link to the feed's home page?
---------------------------------------------------------

Edit ``config.ini`` and add ::

    [http://...feed-url...]
    link = http://fixed-url


How do I fix a feed title?
--------------------------

Edit ``config.ini`` and add ::

    [http://...feed-url...]
    name = Fixed title


How do I add a filter on a particular feed?
-------------------------------------------

Edit ``config.ini`` and add ::

    [http://...feed-url...]
    filters = myfilter.ext

then create ``filters/myfilter.ext``, where ``ext`` selects the filter type
(``xslt``, ``py``, ``plugin``).  The filter gets Atom data in the stdin and is
supposed to emit it on stdout.


How do I test/debug XLST filters?
---------------------------------

Use ::

  xlstproc filters/myfilter.ext - < cache/feed,msgid


How do I pretty-print XML?
--------------------------

Use ::

  xmllint --format cache/feed,msg


How can I git push my changes without entering my password?
-----------------------------------------------------------

Make sure ``.git/config`` has ::

    [remote "origin"]
            fetch = +refs/heads/*:refs/remotes/origin/*
            url = https://github.com/mgedmin/planet-mg
            pushurl = git.github.com:mgedmin/planet-mg.git

Then the cron script can fetch updates via anonymous HTTPS, while you can git
push changes via key-authenticated passwordless SSH.
