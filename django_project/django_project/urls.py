from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^Romulus/', include('Romulus.urls')),
    url(r'^$', 'Romulus.views.index'),

    url(r'^admin/', include(admin.site.urls)),
)
