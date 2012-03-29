"""
If the user is using the CAS app then this will be active and 
the change password fields will be hidden.
"""
from django.conf import settings

def is_using_cas(request):
    
	try:
		exists = settings.BU_ADMIN_USE_CAS
	except:
		exists = False
	
	return {'is_using_cas': exists}