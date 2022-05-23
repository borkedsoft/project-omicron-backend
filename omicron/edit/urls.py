from django.urls import path, include
from . import views
from . import serializers

app_name="edit"

urlpatterns = [
    path('',                                  views.index,    name="index"),
    path('explore/',                          views.explore,  name="explore"),
    path('editor/',                           views.create,   name="createProject"),
    path('editor/<int:projectID>/',           views.editor,   name="editor"),
    path('code/<int:codeID>/',                views.code,     name="code"),
    path('code/<int:projectID>/<str:name>/',  views.projCode, name="projcode"),

    path('api/',                              include(serializers.router.urls)),
]
