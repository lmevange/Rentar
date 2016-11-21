from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.forms import ModelForm, HiddenInput
from rentar.forms import ApartmentForm, ApartmentRatingForm
from rentar.models import Apartment
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login as auth_login,
	logout,
# from django.contrib.auth import authenticate, login

)
from django.views.generic import View
from rentar.forms import UserLoginForm, UserRegisterForm, UserProfileForm

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

def search(request):
	qry_string=''
	found_objects = None
	qry_string = request.GET.get('q')
	if (qry_string !=''):
		results= Apartment.objects.filter(address_line__contains=qry)
	return render(request,'results.html', {"results":results})

def add_apartment(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = ApartmentForm(request.POST)

		if form.is_valid():
			apartment = form.save(commit = True)
			return redirect ('add_apartment_rating', pk = apartment.pk)
		else:
			print (form.errors)
	else:
		form = ApartmentForm()

	return render(request,'add_apartment.html', {'form':form})

def add_apartment_rating(request, pk):
#	context = RequestContext(request)

	if request.method == 'POST':
		form = ApartmentRatingForm(request.POST)

		if form.is_valid():
			rating = form.save(commit = False)
			rating.apartment=Apartment.objects.get(id=pk) 
			rating.save()
			return index(request)
		else:
			print (form.errors)
	else:
		form = ApartmentRatingForm()

	return render(request,'add_apartment_rating.html', {'form':form}) #change name of html after merging maybe

def edit_apartment(request, pk):
	apartment = get_object_or_404(Apartment, pk=pk)
	if request.method == "POST":
		form = ApartmentForm(request.POST, instance=apartment)
		if form.is_valid():
			apartment = form.save(commit = True)
			return index(request)
	else:
		form = ApartmentForm(instance=apartment)
	return render(request, 'add_apartment.html', {'form':form})#possibly make different html for edit

def login_view(request):
	title = "Login"
	oppTitle = "Create Account"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		auth_login(request,user)
		return redirect("/")

	return render(request, "login_form.html", {"form":form, "title": title, "oppTitle": oppTitle})

def register_view(request):
	title = "Register"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()

		new_user = authenticate(username=user.username, password=password)		
		auth_login(request,user)
		return redirect("/") # redirects to homepage after registration 

	context = {
		"form": form,
		"title": title
	}
	return render(request, "registration_form.html", context)

def logout_view(request):
	logout(request)
	return render(request, "index.html", {})

#will be used in the future
def profile_view(request):
	user = request.user
	form = UserProfileForm(initial={'first_name':user.first_name, 'last_name':user.last_name})
	context = {
		"form": form
	}
	return render(request, 'profile.html', context)

def edit_profile(request):
	user = request.user
	form = UserProfileForm(request.POST or None, initial={'first_name':user.first_name, 'last_name':user.last_name})
	if request.method == 'POST':
		if form.is_valid():
			user.username = request.POST['username']
			user.first_name = request.POST['first_name']
			user.last_name = request.POST['last_name']
			user.save()

	context = {
		"form": form,
		"username": user
	}

	return render(request, "edit_profile.html", context)
