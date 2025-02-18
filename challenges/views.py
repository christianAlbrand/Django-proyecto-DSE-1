from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


months_lib = {
    "january" : "Walk for at least 30 min every day.",
    "february" : "Go to the gym every day",
    "march" : "Read one book this month",
    "april": "Start a new programming project",
    "may": "Practice a new skill daily",
    "june": "Go for a morning run every weekend",
    "july": "Learn a new technology or framework",
    "august": "Write a blog post about coding",
    "september": "Contribute to an open-source project",
    "october": "Prepare for a coding challenge",
    "november": "Build a small web application",
    "december": "Review and reflect on the year's progress",
}
# Create your views here.
def index(request):
    return HttpResponse("hasta aqui si funciona")

def monthly_challenge(request, month):

    month_var = months_lib.get(month)

    if month_var:
        return HttpResponse(f"challenge of {month} : {month_var}")
    else:
        return HttpResponseNotFound("Mes no encontrado :c")
    
