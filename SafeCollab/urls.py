from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
                       # url(r'^$', 'SafeCollab.views.home'),
                       url(r'^$', 'home.views.index'),
                       # url(r'^$', 'auth.views.index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/$', 'auth.views.login_user'),
                       url(r'^register/$', 'auth.views.register_user'),
                       url(r'^logout/$', 'auth.views.logout_user'),
                       url(r'^sm/', 'auth.views.list_users'),
                       url(r'^groups/', include('auth.urls', namespace='groups')),
                       url(r'^', include('encrypt.urls', namespace="encrypt")),
                       url(r'^encrypt/$', 'encrypt.views.index'),
                       url(r'^FileUpload/', include('FileUpload.urls')),
                       url(r'^reports/', include('report_database.urls')),
                       #url(r'^$', RedirectView.as_view(url='/FileUpload/list/', permanent=False)),
                       #url(r'^upload/$', 'FileUpload.views.index'),
                       url(r'^messages/', include('django_messages.urls', namespace='messages')),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)