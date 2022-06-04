from django.contrib.auth.models import User
from edit.models import Project, ProjectCode
from rest_framework import routers, serializers, viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse

# https://stackoverflow.com/questions/29362142/django-rest-framework-hyperlinkedidentityfield-with-multiple-lookup-args
# thx SuperDuperTango
class CodeHyperlink(serializers.HyperlinkedIdentityField):
    def to_representation(self, value):
        return reverse('edit:projcode',
                       kwargs={
                           'projectID': value.project_id,
                           'name':      value.name,
                       },
                       request=self.context["request"])

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    codefiles = serializers.HyperlinkedIdentityField(view_name = "edit:projectCodeList")

    class Meta:
        model = Project
        fields = ["name", "date_created", "date_updated", "codefiles"]

class ProjectCodeSerializer(serializers.HyperlinkedModelSerializer):
    codefile = CodeHyperlink(view_name = "edit:projcode")
    codetext = serializers.HyperlinkedIdentityField(view_name = "edit:codeText")

    class Meta:
        model = ProjectCode
        #fields = ["name", "codefile", "date_created", "date_updated"]
        fields = ["name", "codefile", "codetext", "date_created", "date_updated"]

class CodeTextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectCode
        fields = ["code"]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset         = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectCodeViewSet(viewsets.ModelViewSet):
    queryset         = ProjectCode.objects.all()
    serializer_class = ProjectCodeSerializer

class CodeTextViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset         = ProjectCode.objects.all()
    serializer_class = CodeTextSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ProjectCodeList(generics.GenericAPIView):
    queryset         = Project.objects.all()

    def get(self, request, *args, **kwargs):
        proj = self.get_object()
        code = proj.projectcode_set.all()

        proj_serializer = ProjectSerializer(proj, context= {"request": request})
        code_serializer = ProjectCodeSerializer(code, context={"request": request}, many=True)

        return Response(code_serializer.data)

router = routers.DefaultRouter()
router.register(r'projects',    ProjectViewSet)
router.register(r'projectCode', ProjectCodeViewSet)
#router.register(r'codeText',    CodeTextViewSet)

print(list(router.registry))
