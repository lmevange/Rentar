from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context, loader
# Create your views here.
def index(request):
#	return HttpResponse("This is a test")
#	return render_to_response('../../index.html')
#	myFile = open('index.html')-------------------------second try, no luck cant find file
#	data="\n".join(line for line in myFile)
#	return HttpResponse(data)
#	template = loader.get_template("index.html")
#	return HttpResponse(template.render())
	return render(request, 'index.html')
