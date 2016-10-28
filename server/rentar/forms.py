from django import forms
from rentar.models import Apartment, Landlord, Apartment_Rating, Landlord_Rating
class ApartmentForm(forms.ModelForm):
	class Meta:
		model = Apartment
		fields = '__all__'
class LandlordForm(forms.ModelForm):
	class Meta:
		model = Landlord
		fields = '__all__'

class ApartmentRatingForm(forms.ModelForm):
	class Meta:
		model = Apartment_Rating
		fields = '__all__'

class LandlordRatingForm(forms.ModelForm):
	class Meta:
		model = Landlord_Rating
		fields = '__all__'
