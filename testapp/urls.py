from django.urls import path
from . import views

# . --> current folder

# URLConfiguration
urlpatterns = [
    path('hello/', views.say_hello)  # passing a reference to the fuction, not calling it

]
