from django.shortcuts import render
from django.http import HttpResponse

def foobar(request):
    return HttpResponse("Hello, world! Testing this more!")

def index(request):
    return render(request, "edit/main.html", {})

def editor(request):
    return render(request, "edit/editor.html", {})
