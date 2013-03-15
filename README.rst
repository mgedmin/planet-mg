Planet Mg -- Feeds I Read
=========================

You probably heard about Google Reader shutting down.  Before I used Google
Reader I had a Planet feed aggregator running on my website.  This is an
attempt to resurrect that old solution.

Usage::

    sudo apt-get install xsltproc
    git clone https://github.com/mgedmin/planet-mg ~/src/planet-mg
    cd ~/src/planet-mg
    make
    crontab -e
      @hourly make -C $HOME/src/planet-mg update-cron

