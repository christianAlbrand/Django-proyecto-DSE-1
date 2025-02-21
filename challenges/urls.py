from django.urls import path
from . import views

urlpatterns=[
    path("", views.index),
    # path("<int:month>/", views.monthly_challenge_num, name="monthly-challenge-num"),
    path("<str:month>/", views.monthly_challenges, name="monthly-challenge"),

]