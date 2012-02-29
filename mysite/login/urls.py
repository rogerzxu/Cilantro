from django.conf.urls.defaults import patterns, include, url
from mysite.login.views import register, login_view

urlpatterns = patterns('mysite.login.views',
    url(r'^$',login_view ),
    url(r'^register/', register),
#    url(r'^confirm/', confirm),
)
