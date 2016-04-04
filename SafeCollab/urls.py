from django.conf.urls import patterns, include, url
from django.contrib import admin

# admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'SafeCollab.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/$', 'auth.views.login_user'),
                       url(r'^logout/$', 'auth.views.logout_user'),
                       url(r'^', include('encrypt.urls', namespace="encrypt")),
                       url(r'^encrypt/$', 'encrypt.views.index'),
                       )
