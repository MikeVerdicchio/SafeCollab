from django.conf.urls import url, patterns
from . import views


urlpatterns = [
    url(r'^$', views.index, name='report_home'),
    url(r'^create/$', views.create, name='report_create'),
    url(r'^manage/$', views.manage, name='report_manage'),
]