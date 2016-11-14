from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.forms import ModelForm
from rentar.forms import ApartmentForm, LandlordForm, LandlordRatingForm, ApartmentRatingForm
from django.contrib.auth import authenticate, login
from django.views.generic import View
from rentar.forms import UserForm

# Create your views here.
def index(request):
	return render(request, 'index.html')

def login(request):
	return render(request, 'login.html')

def addressview(request):
	return render(request, 'addressview.html')

def contact(request):
	return render(request, 'contact.html')

def rating(request):
	return render(request,'rating.html')

def registration_form(request):
	return render(request,'registration_form.html')

def add_apartment(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = ApartmentForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return add_apartment_rating(request)
		else:
			print (form.errors)
	else:
		form = ApartmentForm()

	return render(request,'add_apartment.html', {'form':form})

def add_landlord(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = LandlordForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else:
			print (form.errors)
	else:
		form = LandlordForm()

	return render(request,'add_landlord.html', {'form':form})

def add_apartment_rating(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = ApartmentRatingForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else:
			print (form.errors)
	else:
		form = ApartmentRatingForm()

	return render(request,'add_apartment_rating.html', {'form':form}) #change name of html after merging maybe

def add_landlord_rating(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = LandlordRatingForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return add_apartment(request)
		else:
			print (form.errors)
	else:
		form = LandlordRatingForm()

	return render(request,'add_landlord_rating.html', {'form':form}) #change name of html after merging maybe

class userFormView(View):
	form_class = UserForm
	template_name = 'template/registration_form.html'

	def get(self,request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user.set_password(password)
			user.save()

			user = autheticate(username=username, password=password)

			if user is not None:

				if user.is_active:

					login(request, user)
					return redirect('rentar:index')

		return render(request, self.template_name, {'form': form})