from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'sitio/home.html')

def about(request):
    return render(request, 'sitio/about.html')
