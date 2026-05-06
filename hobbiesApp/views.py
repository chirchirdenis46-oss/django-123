from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context ={} # purpose if hold a refe to the data
    return render (request,"hobbiesApp/home.html", context)

def about(request):
    context={}
    return render(request,"hobbiesApp/about.html", context)

def contact(request):
    context = {}
    return render(request, "hobbiesApp/contact.html", context)

def project(request):
    context = {""}
    return render(request, "hobbiesApp/project.html", context)

def landig(request):
    context = {}
    return render(request, "hobbiesApp/landing.html", context)