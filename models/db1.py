# -*- coding: utf-8 -*-

# to track user interests
db.define_table('Interests',
	Field('userId','reference auth_user'),
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


# Interests

db.define_table('Travelling',
	Field('userId','reference auth_user')
	)

db.define_table('Movies',
	Field('userId','reference auth_user')
	)

db.define_table('Music',
	Field('userId','reference auth_user')
	)

db.define_table('Fitness',
	Field('userId','reference auth_user')
	)

#Hobbies

db.define_table('Singing',
	Field('userId','reference auth_user')
	)

db.define_table('Dancing',
	Field('userId','reference auth_user')
	)

db.define_table('Photography',
	Field('userId','reference auth_user')
	)

db.define_table('Painting',
	Field('userId','reference auth_user')
	)

db.define_table('Reading',
	Field('userId','reference auth_user')
	)

#Cuisine

db.define_table('Chinese',
	Field('userId','reference auth_user')
	)

db.define_table('SouthIndian',
	Field('userId','reference auth_user')
	)

db.define_table('Continental',
	Field('userId','reference auth_user')
	)

db.define_table('Italian',
	Field('userId','reference auth_user')
	)

#Sports/Fitness

db.define_table('Running',
	Field('userId','reference auth_user')
	)

db.define_table('Swimming',
	Field('userId','reference auth_user')
	)

db.define_table('Badminton',
	Field('userId','reference auth_user')
	)

db.define_table('Cricket',
	Field('userId','reference auth_user')
	)

db.define_table('Basketball',
	Field('userId','reference auth_user')
	)
	
db.define_table('WorkOut',
	Field('userId','reference auth_user')
	)




