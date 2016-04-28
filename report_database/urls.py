from django.conf.urls import url, patterns
from . import views
from .models import Report


urlpatterns = [
    url(r'^$', views.index, name='report_home'),
    url(r'^create/$', views.create, name='report_create'),
    url(r'^manage/$', views.manage, name='report_manage'),
    url(r'^report_edit/(?P<report_pk>.*)$', views.reportedit, name='report_edit'),
    url(r'^folder_edit/(?P<folder_pk>.*)$', views.fedit, name='folder_edit'),
    url(r'^folder_add/(?P<folder_pk>.*)$', views.fadd, name='folder_add'),
    url(r'^folder_remove/(?P<folder_pk>.*)$', views.fremove, name='folder_remove'),
    url(r'^fcreate/$', views.fcreate, name='folder_create'),
    url(r'^fmanage/$', views.fmanage, name='folder_manage'),
]