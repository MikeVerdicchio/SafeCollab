from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SafeCollab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^auth/', include('auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
