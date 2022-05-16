from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        print("Got here")
        return HttpResponse("Did the thing!")
    else:
        return HttpResponse("Post pls")


# Create your views here.
