from django.conf.urls import patterns, url
from lite_app import views

urlpatterns = patterns('',
         url(r'^$', views.index, name='index'),
         url(r'^register/$', views.register, name='register'),
         url(r'^login/$', views.user_login, name='login'),
         url(r'^logout/$', views.user_logout, name='logout'),
         url(r'^profile/$', views.user_profile, name='logout'),
         url(r'^profile/delete_profile/$', views.delete_profile, name='delete_profile'),
         url(r'^contacts/$', views.contacts, name='contacts'),
         )
