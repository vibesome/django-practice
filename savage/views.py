from django.shortcuts import render

# Create your views here.

def home(request):
    context={}
    return render(request, "savage/index.html")

def login(request):
    context={}
    return render(request, "savage/login.html")

def signup(request):
    context={}
    return render(request, "savage/signup.html")