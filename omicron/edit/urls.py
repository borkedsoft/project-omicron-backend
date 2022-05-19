from django.urls import path, include
from . import views

app_name="edit"

urlpatterns = [
    path('',        views.index,  name="index"),
    path('editor/', views.editor, name="editor")
]
