from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Hello, world! Testing this more!")
    return render(request, "edit/main.html", {})

# Create your views here.
