#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from copy import deepcopy

from pelican.settings import DEFAULT_CONFIG


AUTHOR = 'Tal Einat'
SITENAME = 'Tal is Programming'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jerusalem'

DEFAULT_LANG = 'English'

MARKDOWN = deepcopy(DEFAULT_CONFIG['MARKDOWN'])
MARKDOWN['extension_configs'].update({
    'mkdcomments': {},
    # 'tables': {},
})

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'extra/favicon.ico',
    'images',
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'images/favicon.ico'},
}

# Theme Settings
THEME = 'brutalist'
## used for OG tags and Twitter Card data on index page
#SITEIMAGE = ''
## used for OG tags and Twitter Card data of index page
SITEDESCRIPTION = 'Tal Einat\'s Programming Blog'
## path to favicon
FAVICON = 'favicon.ico'
## path to logo for nav menu (optional)
#LOGO = 'pelly.png'
## first name for nav menu if logo isn't provided
FIRST_NAME = 'Tal'
## google analytics (fake code commented out)
# GOOGLE_ANALYTICS = 'UA-0011001-1'
## Twitter username for Twitter Card data
TWITTER_USERNAME = '@taleinat'
## Toggle display of theme attribution in the footer (scroll down and see)
## Attribution is appreciated but totally fine to turn off!
ATTRIBUTION = False
## Add a link to the tags page to the menu
## Other links can be added following the same tuple pattern
MENUITEMS = [
    # ('tags', '/tags'),
]
## Social icons for footer
## Set these to whatever your unique public URL is for that platform
## I've left mine here as a example
#STRAVA = 'https://www.strava.com/athletes/27234301'
TWITTER = 'https://twitter.com/taleinat'
#INSTAGRAM = 'https://instagram.com/mcman_s'
GITHUB = 'https://github.com/taleinat'
#TELEGRAM = 'https://t.me/mcman_s'
#GOODREADS = 'https://www.goodreads.com/user/show/48849158-matthew-mcmanus'
#FOURSQUARE = 'https://foursquare.com/mcman_s'
#UNTAPPD = 'https://untappd.com/user/mcman_s'
LINKEDIN = 'https://www.linkedin.com/in/taleinat'
## Disqus Sitename for comments on posts
## Commenting mine out for this theme site
#DISQUS_SITENAME = 'brutalistpelican'
## Gravatar
GRAVATAR = 'https://www.gravatar.com/avatar/cd6aae9615c3b36130e2470902833a72?s=256'
