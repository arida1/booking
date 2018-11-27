from django.conf.urls import url
from . import views

urlpatterns = [
	url('users/', views.user_list, name='user_list'),
	url(r'^$', views.cinema_list, name='cinema_list'),
	url(r'^cinemas/(?P<pk>\d+)/$', views.cinema_detail, name='cinema_detail'),
	url(r'^cinemas/(?P<pk>\d+)/(?P<pk1>\d+)/$', views.ticket_list, name='ticket_list'),
]
