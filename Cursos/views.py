
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Cursos.models import Alumnos, Clases
from rest_framework import viewsets
from Cursos.serializers import AlumnosSerializer, CursosSerializer

class CursosViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Clases.objects.all()
    serializer_class = CursosSerializer

    def list(self,request,*args,**kwargs):
        item_user_ownwer = Clases.objects.filter(owner_user=self.request.user)
        serializer = self.get_serializer(item_user_ownwer,many=True)
        return Response(serializer.data)

class AlumnosViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=Alumnos.objects.all()
    serializer_class = AlumnosSerializer
