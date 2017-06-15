from django.conf.urls import url

from . import views


app_name = 'userauthentication'
urlpatterns = [
	url(r'^reg/$', views.register, name='register'),
	url(r'^$', views.index, name='index'),
	url(r'^log/$', views.user_login, name='login'),
	url(r'^logpage/$', views.login_page, name='login_page'),
	url(r'^logout/$', views.user_logout, name='user_logout'),
	url(r'^(?P<id>\d+)/list/$', views.list, name='list'),


]
