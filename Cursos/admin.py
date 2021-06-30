from django.contrib import admin

# Register your models here.
from Cursos.models import Clases, Alumnos

admin.site.register(Clases)
admin.site.register(Alumnos)