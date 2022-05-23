from django.contrib.auth.models import User
from edit.models import Project, ProjectCode
from rest_framework import routers, serializers, viewsets

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ["name", "date_created", "date_updated"]

class ProjectCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectCode
        fields = ["name", "code", "date_created", "date_updated"]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset         = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectCodeViewSet(viewsets.ModelViewSet):
    queryset         = ProjectCode.objects.all()
    serializer_class = ProjectCodeSerializer

router = routers.DefaultRouter()
router.register(r'projects',    ProjectViewSet)
router.register(r'projectCode', ProjectCodeViewSet)
