
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^addressview/$', views.addressview, name='addressview'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^login/$', views.login, name='login'),
	url(r'^$', views.index, name='index'),
]
