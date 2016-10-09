
from django.conf.urls import url
from . import views

urlpatterns = [
#	url(r'^$', views.addressview, name='addressview'),
#	url(r'^$', views.contact, name='contact'),
#	url(r'^$', views.login, name='login'),
	url(r'^$', views.index, name='index'),
]
