from django import forms
from rentar.models import Apartment, Landlord
class ApartmentForm(forms.ModelForm):
	class Meta:
		model = Apartment
		fields = ['address_text', 'years_lived', 'security_deposit']
class LandlordForm(forms.ModelForm):
	class Meta:
		model = Landlord
		fields = '__all__'
