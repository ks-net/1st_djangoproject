'''
@author: ks-net
'''
from django.conf import settings

def sitedictionary(request):
    site_dict = {
        'site_url': settings.SITE_URL,
        'site_name': settings.SITE_NAME,
    }
    return site_dict
