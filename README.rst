Planet Mg — Feeds I Read
========================

You probably heard about Google Reader shutting down.  Before I used Google
Reader I had a Planet feed aggregator running on my website.  This is an
attempt to resurrect that old solution.

Usage::

    sudo apt-get install git make xsltproc python-virtualenv
    git clone https://github.com/mgedmin/planet-mg ~/src/planet-mg
    cd ~/src/planet-mg
    make
    crontab -e
      @hourly cd $HOME/src/planet-mg && make update-cron

Now expose ``~/src/planet-mg/output`` to the web, e.g. using Apache ::

    ScriptAlias /planet/add /home/mg/src/planet-mg/cgi-bin/add.py
    Alias       /planet     /home/mg/src/planet-mg/output/

