
from django.conf.urls import url
from . import views
#from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.index, name='index'),
#	url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
]
