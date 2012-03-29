===========
BU Django Admin
===========

A BU branded skin over the built-in Django Admin.

-----------
Requirements
-----------

1. Add 'django_buadmin' to INSTALLED_APPS

If you are also using the BU Django CAS middleware and would like to modify the admin templates to remove the change password links and fields, there are two additional steps:

1. Add 'django_buadmin.context_processors.is_using_cas' to your TEMPLATE_CONTEXT_PROCESSORS dict
2. Add the following setting to settings.py: 'BU_ADMIN_USE_CAS = True'

This will add a new variable to your templates -- is_using_cas -- which can be used to make conditional changes to your templates based on the value of the BU_ADMIN_USE_CAS setting.