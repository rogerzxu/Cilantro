from django.conf.urls.defaults import *
from mysite.portal.views import *

urlpatterns = patterns('',

    # Main web portal entrance.
    (r'^$', portal_main_page),

)

