from rest_framework import serializers
from Cursos.models import Clases, Alumnos, Maestros


class CursosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clases
        fields = "__all__"


class AlumnosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alumnos
        fields = "__all__"


class MaestrosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Maestros
        fields = '__all__'
