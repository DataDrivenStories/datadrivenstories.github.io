
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sreenath R Yettapu'
SITENAME = u"""<b><span style="color:#AA1032;">S</span><span style="color:black;">ree</span><span style="color:#AA1032;">A</span><span style="color:black;">nalytics</span></b>"""
SITEURL = 'http://localhost:8000'

PATH = 'content'

# Regional Settings
TIMEZONE = 'Europe/Paris'
DATE_FORMATS = {'en': '%b %d, %Y'}
DEFAULT_LANG = 'English'

MARKUP = ('md', 'ipynb')


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.headerid': {},
        'markdown.extensions.toc': {'permalink': 'true'},
    },
    'output_format': 'html5',
}

PLUGIN_PATHS = ['plugins/']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'liquid_tags.img',
           'neighbors', 'render_math', 'related_posts', 'assets', 'share_post',
           'series', 'ipynb.markup']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Appearance
TYPOGRIFY = True
THEME = 'themes/elegant'
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = u'{slug}'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'

# Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social
SOCIAL = (
        ('Twitter', 'https://twitter.com/SreeAnalytics'),
        ('Github', 'http://github.com/SreeAnalytics'),
        ('Email', 'mailto:sreenath.yettapu@outlook.com'),
        )

# Elegant theme
STATIC_PATHS = ['theme/images', 'images']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = u'Stay in Touch'
RELATED_POSTS_LABEL = 'Keep Reading'
SHARE_POST_INTRO = 'Like this post? Share on:'
COMMENTS_INTRO = u'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'

# Mailchimp
#EMAIL_SUBSCRIPTION_LABEL = u'Get Monthly Updates'
#EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
#SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
#MAILCHIMP_FORM_ACTION = u'empty'

# SMO
#TWITTER_USERNAME = u'SreeAnalytics'
#FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'

# Legal
SITE_LICENSE = u'<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">SreeAnalytics</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://oncrashreboot.com" property="cc:attributionName" rel="cc:attributionURL">Sreenath R Yettapu</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.'

# SEO
SITE_DESCRIPTION = u'My name is Sreenath R Yettapu. This is my personal blog.'

# Landing Page
PROJECTS = [
        	{
            'name': 'Project1',
            'url': 'http://localhost:8000',
            'description': 'project description '
            	' test test test'
        	}
		]

LANDING_PAGE_ABOUT = {
		'title': 'My journey to becoming Machine Learning Engineer',
        'details': """

			<div itemscope itemtype="http://schema.org/Person">
	    		<p>
		    		My name is <span itemprop="name">Sreenath R Yettapu</span>. I am <a href="https://github.com/sreeanalytics/" title="My Github 
		    		profile" itemprop="url"><span itemprop="nickname">sreeanalytics</span></a> at Github and <a href="https://twitter.com/sreeanalytics/" 
		    		title="My Twitter profile" itemprop="url">@sreeanalytics</a> at twitter. You can also reach me via 
		    		<a href="mailto:sreenath.yettapu@gmail.com" title="My email address" itemprop="email">email</a>.
	    		</p>

			</div>

		"""
		}
