from django.conf.urls import url, patterns
from . import views
from .models import Report


urlpatterns = [
    url(r'^$', views.index, name='report_home'),
    url(r'^create/$', views.create, name='report_create'),
    url(r'^manage/$', views.manage, name='report_manage'),
    url(r'^report_edit/(?P<report_pk>.*)$', views.reportedit, name='report_edit'),
]