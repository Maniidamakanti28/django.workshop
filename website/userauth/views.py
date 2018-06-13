from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# Create your views here.

def register(request):
	if request.method == 'POST':
	        form = UserCreationForm(requets.POST)
	        if form.is_valid():
	        	     form.save()
	        	     return HttpResponse("user saved")
	else:       
	        form = UserCreationForm()
	return render(request,'userauth/register.html',{'form':form})

