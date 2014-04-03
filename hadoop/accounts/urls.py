from django.conf.urls import patterns, url
from views import login

urlpatterns = patterns('',
    url(r'login/$', login),
)