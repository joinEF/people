from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'people.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index),
    url(r'^projects/$', views.projects),

    (r'^avatar/', include('avatar.urls')),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}, name="logout"),
    url(r'^accounts/join/$', views.join, name="join"),
    url(r'^accounts/manage/$', views.manage_account),

    url(r'^feedback/$', views.feedback),

    url(r'^(?P<username>\w+)/(?P<project_name>\w+)$', views.project, name='project'),

    url(r'^(?P<username>\w+)$', views.profile, name='profile'),
)
