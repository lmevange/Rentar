from django.shortcuts import render
# from django.forms import ApartmentForm
from rentar.ModelForm import ApartmentForm

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

def add_apartment (request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = ApartmentForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else:
			print (form.errors)
	else:
		form = ApartmentForm()

	return render_to_response('add_apartment.html', {'form':form}, context)
