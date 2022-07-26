from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# a request handler, not actually a view!
# a view function takes a request and returns a response


def say_hello(request):
    # We can pull data from a Database
    # We can transform data
    return HttpResponse('Hello there!')
