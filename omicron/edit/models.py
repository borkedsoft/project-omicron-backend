from django.db import models

class Project(models.Model):
    name         = models.CharField(max_length=255)
    date_created = models.DateTimeField("date_created")
    date_updated = models.DateTimeField("date_updated")

class ProjectCode(models.Model):
    name         = models.CharField(max_length=255)
    #filepath     = models.CharField(max_length=255)
    code         = models.CharField(max_length=8192, default="")
    project      = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_created = models.DateTimeField("date_created")
    date_updated = models.DateTimeField("date_updated")
