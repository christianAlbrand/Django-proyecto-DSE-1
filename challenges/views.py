from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hasta aqui si funciona!")

def january(request):
    return HttpResponse("Walk for at least 30 min every day.")

def february(request):
    return HttpResponse("Go to the gym every day")

def march(request):
    return HttpResponse("Read one book this month")

def april(request):
    return HttpResponse("Start a new programming project")

def may(request):
    return HttpResponse("Practice a new skill daily")

def june(request):
    return HttpResponse("Go for a morning run every weekend")

def july(request):
    return HttpResponse("Learn a new technology or framework")

def august(request):
    return HttpResponse("Write a blog post about coding")

def september(request):
    return HttpResponse("Contribute to an open-source project")

def october(request):
    return HttpResponse("Prepare for a coding challenge")

def november(request):
    return HttpResponse("Build a small web application")

def december(request):
    return HttpResponse("Review and reflect on the year's progress")
