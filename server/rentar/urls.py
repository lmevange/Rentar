
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^add_landlord/$', views.add_landlord, name='add_landlord'), # NEW MAPPING!	
	url(r'^add_landlord_rating/$', views.add_landlord_rating, name='add_landlord_rating'), # NEW MAPPING!	
	url(r'^add_apartment_rating/$', views.add_apartment_rating, name='add_apartment_rating'), # NEW MAPPING!	
	url(r'^add_apartment/$', views.add_apartment, name='add_apartment'), # NEW MAPPING!	
	url(r'^addressview/$', views.addressview, name='addressview'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^login/$', views.login, name='login'),
	url(r'^rating/$',views.rating, name='rating'),
	url(r'^$', views.index, name='index'),
	url(r'^opinion_form/$', views.opinion_form, name = 'opinion_form'),
]
