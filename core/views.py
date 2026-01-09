# Create your views here.
from django.shortcuts import render
from datetime import datetime

def services(request):
    return render(request, 'services.html')

def home(request):
    return render(request, 'home.html', {'year': datetime.now().year})

def about(request):
    return render(request, 'about.html', {'year': datetime.now().year})

def contact(request):
    return render(request, 'contact.html', {'year': datetime.now().year})
