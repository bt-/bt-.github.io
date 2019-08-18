#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ben Taylor'
SITENAME = 'BT Archives'
# SITEURL = ''
SITEURL = 'http://bt-.github.io'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

LOAD_CONTENT_CACHE = False
DISPLAY_PAGES_ON_MENU = 'True'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Brutalist theme settings
THEME = 'brutalist'
## used for OG tags and Twitter Card data on index page
SITEIMAGE = 'headshot.jpg'
## used for OG tags and Twitter Card data of index page
SITEDESCRIPTION = 'Posts documenting my experience learning python and developing a python package.'
## path to favicon
#FAVICON = 'pelly.png' # commented out default from theme
## path to logo for nav menu (optional)
LOGO = 'headshot.jpg'
## first name for nav menu if logo isn't provided
FIRST_NAME = 'bt-'
## google analytics (fake code commented out)
# GOOGLE_ANALYTICS = 'UA-0011001-1'
## Twitter username for Twitter Card data
TWITTER_USERNAME = '@mcman_s'
## Toggle display of theme attribution in the footer (scroll down and see)
## Attribution is appreciated but totally fine to turn off!
ATTRIBUTION = True
## Add a link to the tags page to the menu
## Other links can be added following the same tuple pattern
MENUITEMS = [('tags', '/tags')]
## Social icons for footer
## Set these to whatever your unique public URL is for that platform
## I've left mine here as a example
TWITTER = 'https://www.twitter.com/benjaming_t'
GITHUB = 'https://github.com/bt-'
LINKEDIN = 'https://www.linkedin.com/in/benjamin-taylor-1485a2b'
