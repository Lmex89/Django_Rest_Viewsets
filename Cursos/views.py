
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from Cursos.models import Alumnos, Clases
from rest_framework import viewsets
from Cursos.serializers import AlumnosSerializer, CursosSerializer

class CursosViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Clases.objects.all()
    serializer_class = CursosSerializer


class AlumnosViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=Alumnos.objects.all()
    serializer_class = AlumnosSerializer
