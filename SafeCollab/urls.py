from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'SafeCollab.views.home', name='home'),
    url(r'^$', 'home.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'auth.views.login_user'),
    url(r'^logout/$', 'auth.views.logout_user'),
    url(r'^', include('encrypt.urls', namespace="encrypt")),
    url(r'^encrypt/$', 'encrypt.views.index'),
    url(r'^FileUpload/',include('FileUpload.urls')),
    url(r'^$', RedirectView.as_view(url='/FileUpload/list/', permanent=True)),
    #url(r'^upload/$', 'FileUpload.views.index'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# admin.autodiscover()

