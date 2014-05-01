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

    url(r'^projects/new/$', views.edit_project, name='new_project'),
    url(r'^projects/(?P<project_id>\d+)/[\w-]+/edit/$', views.edit_project, name='edit_project'),
    url(r'^projects/(?P<project_id>\d+)/[\w-]+/delete/$', views.delete_project, name='delete_project'),
    url(r'^projects/(?P<project_id>\d+)/', views.view_project, name='view_project'),

    url(r'^(?P<username>\w+)/$', views.profile, name='profile'),
)
