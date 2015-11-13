# -*- coding: utf-8 -*-

# to track user interests
db.define_table('Interests',
	Field('userId','reference auth_user',unique=True,readable=False,writable=False),
	Field('Singing','text',requires=IS_IN_SET(('Yes','No'))),
	Field('Dancing','text',requires=IS_IN_SET(('Yes','No'))),
	Field('Phtography','text',requires=IS_IN_SET(('Yes','No'))),
	Field('Painting','text',requires=IS_IN_SET(('Yes','No'))),
	Field('Reading','text',requires=IS_IN_SET(('Yes','No'))),
	Field('Travelling','text',requires=IS_IN_SET(('Yes','No'))),
	Field('Movies','text',requires=IS_IN_SET(('Yes','No'))),
	Field('Music','text',requires=IS_IN_SET(('Yes','No'))),
	Field('Fitness','text',requires=IS_IN_SET(('Yes','No'))),
	Field('Running','text',requires=IS_IN_SET(('Yes','No'))),
	Field('Swimming','text',requires=IS_IN_SET(('Yes','No'))),
	Field('Badminton','text',requires=IS_IN_SET(('Yes','No'))),
	Field('Cricket','text',requires=IS_IN_SET(('Yes','No'))),
	Field('Basketball','text',requires=IS_IN_SET(('Yes','No'))),
	Field('WorkOut','text',requires=IS_IN_SET(('Yes','No'))),
	Field('SouthIndian','text',requires=IS_IN_SET(('Yes','No'))),
	Field('Chinese','text',requires=IS_IN_SET(('Yes','No'))),
	Field('Continental','text',requires=IS_IN_SET(('Yes','No'))),
	Field('Italian','text',requires=IS_IN_SET(('Yes','No')))
	)




