Some problems I've solved
=========================


Q: Can I define a feed in sources.xml then override something in config.ini?
----------------------------------------------------------------------------

**A:** Yes.  Just add ::

   [http://...feed-url...]
   ...overrides...

to ``config.ini``.  When testing, don't forget to remove the cached *source*
(see next question)!


Q: How do I test feed settings changes in config.ini?
-----------------------------------------------------

**A:** Do ::

    rm cache/sources/...feed...*
    bin/planet -n

This is necessary because many of the settings take effect during input
processing, which happens only when you fetch new content for the feed.


Q: How do I fix a feed that keeps floating its entries to the top
-----------------------------------------------------------------

**A:** Edit ``config.ini`` and add ::

    [http://...feed-url...]
    ignore_in_feed = updated


Q: How do I add a missing link link to the feed's home page?
------------------------------------------------------------

**A:** Edit ``config.ini`` and add ::

    [http://...feed-url...]
    link = http://fixed-url


Q: How do I fix a feed title?
-----------------------------

**A:** Edit ``config.ini`` and add ::

    [http://...feed-url...]
    name = Fixed title


Q: How can I git push my changes without entering my password?
--------------------------------------------------------------

**A:** Make sure ``.git/config`` has ::

    [remote "origin"]
            fetch = +refs/heads/*:refs/remotes/origin/*
            url = https://github.com/mgedmin/planet-mg
            pushurl = git.github.com:mgedmin/planet-mg.git

Then the cron script can fetch updates via anonymous HTTPS, while you can git
push changes via key-authenticated passwordless SSH.

