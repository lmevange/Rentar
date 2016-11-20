from rentar.models import Apartment, Apartment_Rating
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

)
class ApartmentForm(forms.ModelForm):
	class Meta:
		model = Apartment
		fields = '__all__'


class ApartmentRatingForm(forms.ModelForm):
    class Meta:
        model = Apartment_Rating
        fields = '__all__'

#User profile information

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("Wrong username or password")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")

            if not user.is_active:
                raise forms.ValidationError("This user is no longer active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email Address')    
    emailConfirm = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'emailConfirm', 'username', 'password']

    #the below code will spit out an error to the given field
    def clean_email2(self): #make sure emails match
        email = self.cleaned_data.get('email')
        emailConfirm = self.cleaned_data.get('emailConfirm')
        if email != emailConfirm:
            raise forms.ValidationError("Emails must match")

        email_qs = User.objects.filter(email=email) 
        if email_qs.exists(): #check if email already exists in database
            raise forms.ValidationError("This email has already been registered")
        return email

    #the below code will spit out the error to the top.
    #uncomment and comment the above if you rather use the bottom feature
    #it will be redundent to have both lol but whatevs

    # def clean(self, *args, **kwargs): #make sure emails match
    #     email = self.cleaned_data.get('email')
    #     emailConfirm = self.cleaned_data.get('emailConfirmed')
    #     if email != emailConfirmed:
    #         raise forms.ValidationError("Emails must match")

    #     email_qs = User.objects.filter(email=email) 
    #     if email_qs.exists(): #check if email already exists in database
    #         raise forms.ValidationError("This email has already been registered")
    #     return super(UserRegisterForm,self).clean(*args, **kwargs)

class UserProfileForm(forms.ModelForm):
    username = forms.CharField(label='Username')        #allows user to change username
    first_name = forms.CharField(label='First Name')    #allows user to add/edit first name
    last_name = forms.CharField(label='Last Name')      #allows user to add/edit last name

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name']
