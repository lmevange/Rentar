from django import forms
from rentar.models import Apartment, Landlord
class ApartmentForm(forms.ModelForm):
	class Meta:
		model = Apartment
		fields = '__all__'
class LandlordForm(forms.ModelForm):
	class Meta:
		model = Landlord
		fields = '__all__'
