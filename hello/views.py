from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def gracane(request):
    return HttpResponse("Hello, Graçane")

def muhate(request):
    return HttpResponse("Hello, Muhate")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })