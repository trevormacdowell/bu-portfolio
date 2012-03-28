from distutils.core import setup

setup(
	name='bu-django-admin',
	version='0.1.0',
	author='Tyler Wiest',
	author_email='jtwiest@bu.edu',
	packages=['django_buadmin',],
	url='http://github.com/bu-ist/bu-django-admin',
	license='LICENSE.txt',
	description='A BU branded skin for the built-in Django Admin',
	long_description=open('README.rst').read(),
	install_requires=[
		"Django >= 1.1.1",
	],
)
