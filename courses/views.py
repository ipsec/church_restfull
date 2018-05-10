# Create your views here.
from rest_framework import viewsets

from courses.models import StudentClass
from courses.serializers import ClassSerializer


class ClassViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows class to be viewed or edited.
    """
    queryset = StudentClass.objects.all().order_by('title')
    serializer_class = ClassSerializer

