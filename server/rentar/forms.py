
from django import forms
from django.contrib.auth.models import User
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


#User profile information

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
		model = User
		fields = ['username','email', 'password']
