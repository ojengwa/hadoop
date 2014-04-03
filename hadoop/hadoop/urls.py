from django.conf.urls import patterns, include, url
from accounts.views import login
from views import index, hello

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hadoop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',  index),
    url(r'^hello$', hello),
    url(r'^accounts/', include('accounts.urls')),
)
