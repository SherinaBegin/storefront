#map urls to our view funtions
from django.urls import path
from . import views

#URL Configuration every app can have its own url config

urlpatterns = [
   path('hello/', views.say_hello )
]