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

defaultMain="""
// entry point for your code, called once per frame.
export function loop(delta) {
    console.log('testing this! ' + delta);
}
"""

defaultNew="""export default function yourFunction() {
    /* Your code here */
}
"""

def create(request):
    name = "Unnamed project"
    now = timezone.now()
    p = Project(name=name, date_created=now, date_updated=now)
    p.save()

    p.projectcode_set.create(name="main.js",
                             code=defaultMain,
                             date_created=timezone.now(),
                             date_updated=timezone.now())

    return HttpResponseRedirect(reverse("edit:editor", kwargs={"projectID": p.id}))

def createFile(request, pk):
    error = None

    if not request.user.is_authenticated:
        error = "You are not logged in!"

    elif "filename" not in request.POST:
        error = "Filename field not included in the post request."

    elif len(request.POST["filename"]) == 0:
        error = "No filename provided."
    
    if error:
        return HttpResponse(error)

    else:
        newname = request.POST["filename"]

        if newname[-3:] != ".js":
            newname += ".js"

        proj = get_object_or_404(Project, pk=pk)
        proj.projectcode_set.create(name=newname,
                                    code=defaultNew,
                                    date_created=timezone.now(),
                                    date_updated=timezone.now())

        return HttpResponse("File created")

# return the javascript code corresponding to the given code ID
def code(request, pk):
    code = get_object_or_404(ProjectCode, pk=pk)
    return HttpResponse(code.code, headers = {
        "Content-Type":  "text/javascript",
        "Cache-Control": "no-cache",
    })

# return javascript code contained in a project by name (used for javascript imports)
def projCode(request, projectID, name):
    proj = get_object_or_404(Project, pk=projectID)
    code = get_object_or_404(proj.projectcode_set, name=name)
    return HttpResponse(code.code, headers = {
        "Content-Type": "text/javascript",
        "Cache-Control": "no-cache",
    })

# XXX: nocache is fake directory name generated randomly by the client
#      to avoid module caching (so that all modules are always reloaded)
def projCodeNocache(request, projectID, nocache, name):
    return projCode(request, projectID, name)
