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

# def monthly_challenge(request, month):

#     month_var = months_lib.get(month)

#     if month_var:
#         return HttpResponse(f"challenge of {month} : {month_var}")
#     else:
#         return HttpResponseNotFound("Mes no encontrado :c")

# def monthly_challenge_num(request, month):
#     months_list = list(months_lib.keys())
#     if months_list[month]:
#         return HttpResponse(f"Challenge of {months_list[month]} :{months_lib.get(months_list[month])}")
#     else:
#         return HttpResponseNotFound("Mes no encontrado")

def monthly_challenges(request, month):
    try:
        challenge_text = months_lib[month]
        return render(request,"challenges/challenge.html",{
            "text" : challenge_text,
            "month_name": month
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

