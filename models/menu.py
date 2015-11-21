# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('iConnect'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href=URL('default','index'))
                  
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = []

if auth.user!=None:
	if auth.user.first_name!='admin':
		response.menu.append((T('Home'), False, URL('default', 'homeFree'), []))
		response.menu.append((T('My Profile'),False, URL('default','myProfileFree'),[]))
		response.menu.append((T('My Wishlist'),False,URL('default','wishList'),[]))
		response.menu.append((T('Full List'),False,URL('default','fullList'),[]))


DEVELOPMENT_MENU = True


if "auth" in locals(): auth.wikimenu() 
