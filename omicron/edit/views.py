from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from edit.models import Project, ProjectCode

def foobar(request):
    return HttpResponse("Hello, world! Testing this more!")

def index(request):
    return render(request, "edit/main.html")

def editor(request, projectID):
    proj = get_object_or_404(Project, pk=projectID)
    return render(request, "edit/editor.html", { "project": proj, })

def explore(request):
    return render(request, "edit/explore.html", {
            "projects": Project.objects.all()
        })

def create(request):
    name = "Unnamed project"
    now = timezone.now()
    p = Project(name=name, date_created=now, date_updated=now)
    p.save()
    return HttpResponseRedirect(reverse("edit:editor", kwargs={"projectID": p.id}))

# return the javascript code corresponding to the given code ID
def code(request, codeID):
    code = get_object_or_404(ProjectCode, pk=codeID)
    return HttpResponse(code.code, headers = { "Content-Type": "text/javascript" })

# return javascript code contained in a project by name (used for javascript imports)
def projCode(request, projectID, name):
    proj = get_object_or_404(Project, pk=projectID)
    code = get_object_or_404(proj.projectcode_set, name=name)
    return HttpResponse(code.code, headers = { "Content-Type": "text/javascript" })
