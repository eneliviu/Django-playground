from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):  # the view here is called 'index' if the URL router (urls.py) finds a match
    return HttpResponse("Hello, world!")  # this goes to the browser

