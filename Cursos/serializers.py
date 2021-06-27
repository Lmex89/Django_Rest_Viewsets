from rest_framework import serializers
from rest_framework.response import Response
from Cursos.models import Clases,Alumnos

class CursosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Clases
        fields = '__all__'


class AlumnosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alumnos
        fields = '__all__'