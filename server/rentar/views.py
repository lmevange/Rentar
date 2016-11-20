from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.forms import ModelForm
from rentar.forms import ApartmentForm, ApartmentRatingForm
from rentar.models import Apartment

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
	context = RequestContext(request)

	if request.method == 'POST':
		form = ApartmentRatingForm(request.POST)

		if form.is_valid():
			rating = form.save(commit = False)
			rating.id=pk
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
