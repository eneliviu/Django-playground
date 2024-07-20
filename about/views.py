from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about_me(request): # request contains metadata about the request made to the browser
    return HttpResponse("This would be the about page")