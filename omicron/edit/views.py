from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! Return the frontend stuff pls!")

# Create your views here.
