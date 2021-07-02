
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import status
from Cursos.models import Alumnos, Clases
from Cursos.serializers import AlumnosSerializer, CursosSerializer


class CursosViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Clases.objects.all()
    serializer_class = CursosSerializer

    def get_queryset(self, request):
        data ={ key:value for key, value in self.request.query_params.items() if key not in ['page']}

        return self.queryset.filter(**data)

    def list(self,request,*args,**kwargs):
        #item_user_ownwer = Clases.objects.filter(owner_user=self.request.user)
        item = self.get_queryset(request)
        page = self.paginate_queryset(item)
        if page:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(item, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['DELETE','POST'])
    def alumnos_add_delete(self,request,pk=None):
        clase = self.get_object()
        if self.request.method == 'POST':
            list_names = request.data['alumno_name']
            print(list_names)
            alumnos_post = Alumnos.objects.filter(pk__in=list_names)
            print(alumnos_post)
            for alumno in alumnos_post:
                clase.alumnos.add(alumno)

            return Response(status=status.HTTP_200_OK)
        if self.request.method == 'DELETE':
            list_names = request.data['alumno_name']
            alumno = Alumnos.objects.filter(nombre__in=request.data['alumno_name'])
            alumno.delete()
            print(clase.alumnos)
            return Response(status=status.HTTP_200_OK)


class AlumnosViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=Alumnos.objects.all()
    serializer_class = AlumnosSerializer
