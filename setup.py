from distutils.core import setup

setup(
	name='bu-django-admin',
	version='0.1.0',
	author='Tyler Wiest',
	author_email='jtwiest@bu.edu',
	packages=['django_bucas',],
	url='http://github.com/bu-ist/django-bu-cas',
	license='LICENSE.txt',
	description='CAS Authentication middleware for the BU Django environment',
	long_description=open('README').read(),
	install_requires=[
		"Django >= 1.1.1",
	],
)
