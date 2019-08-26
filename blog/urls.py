from django.conf.urls import url
from . import views
from . import views_client

urlpatterns = [
    #RUTAS DEL BLOG
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/', views.post_remove, name='post_remove'),

    #RUTAS DEL CLIENTE
    url(r'^client/list/$', views_client.client_list, name='client_list'),
    url(r'^client/new/$', views_client.client_new, name='client_new'),
    url(r'^client/(?P<pk>\d+)/edit/$', views_client.client_edit, name='client_edit'),
    url(r'^client/(?P<pk>\d+)/remove/', views_client.client_remove, name='client_remove'),
]

