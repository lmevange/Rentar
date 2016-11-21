from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^registration_form/$', views.registration_form, name='registration_form'),
	url(r'^edit_apartment/(?P<pk>\d+)/$', views.edit_apartment, name='edit_apartment'),
	url(r'^add_apartment_rating/(?P<pk>\d+)/$', views.add_apartment_rating, name='add_apartment_rating'), 
	url(r'^add_apartment/$', views.add_apartment, name='add_apartment'),	
	url(r'^apartment_view/(?P<pk>\d+)/$', views.apartment_view, name='apartment_view'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^login/$', views.login_view, name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^register/$', views.register_view, name='register'),
	url(r'^rating/$',views.rating, name='rating'),
	url(r'^profile/$', views.profile_view, name='profile'),
	url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
	url(r'^$', views.index, name='index'),
]
