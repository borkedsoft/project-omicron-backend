from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os

@csrf_exempt
def index(request):
    if request.method == "POST":
        print("Got here")
        # XXX: hax
        os.system("./deploy.sh &")
        return HttpResponse("Did the thing!")
    else:
        return HttpResponse("Post pls")
