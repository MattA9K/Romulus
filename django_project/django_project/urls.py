from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^Romulus/', include('Romulus.urls')),
    url(r'^test', 'Romulus.views.test'),
    url(r'^BrandiLove', 'Romulus.views.index'),
    url(r'^Secret', 'Romulus.views.index'),
    url(r'^$', 'Romulus.views.authorize_access'),

    url(r'^admin/', include(admin.site.urls)),
)
