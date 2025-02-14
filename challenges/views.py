from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hasta aqui si funciona!")

def january(request):
    return HttpResponse("Walk for at least 30 min every day.")

def february(request):
    return HttpResponse("Go to the gym every day")