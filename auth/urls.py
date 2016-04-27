from django.conf.urls import url, patterns
from . import views

urlpatterns = [
    url(r'^$', 'auth.views.manage_group'),
    url(r'^group_info/(?P<name>.*)$', views.show_group, name='show_group'),
    url(r'^create/$', views.create_group, name='create_group'),
]