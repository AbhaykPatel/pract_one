from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
#def group(request):
   # return HttpResponse("group called...")

def index(request):
    return render(request, 'owner/index.html')

def aboutus(request):
    return  render(request, 'owner/aboutus.html')

def contactUs(request):
    return render(request, 'owner/contactUs.html')