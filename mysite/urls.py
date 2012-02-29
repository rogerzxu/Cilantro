from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from mysite.views import my_homepage_view, logout_page

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from mysite.settings import *




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^polls/', include('mysite.polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^login/', include('mysite.login.urls')),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^portal/', include('mysite.portal.urls')),
    (r'^$', my_homepage_view),
    
  #  (r'^images/$', image_page),
   # (r'^static/', 'django.views.static.serve',
    #    {'document_root': 'static'}),
    
)

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
