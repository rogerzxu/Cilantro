from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('mysite.login.views',
    url(r'^$', 'index'),
)
