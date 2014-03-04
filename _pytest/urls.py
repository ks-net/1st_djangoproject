from django.conf.urls import patterns, include, url

from django.conf.urls.i18n import i18n_patterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pytest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
        
    url(r'^blog/', include('blog.urls', namespace="blog")),
    
    # Add (r'^admin/doc/', include('django.contrib.admindocs.urls')) to your urlpatterns. 
    # Make sure it is before admin/ entry, so that requests 
    # to /admin/doc/ don't get handled by the latter entry.
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),     
)

urlpatterns += i18n_patterns('',
    url(r'^blog/', include('blog.urls', namespace="blog")), 
)