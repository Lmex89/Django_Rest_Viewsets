from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
import uuid


class Alumnos(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True)
    nombre = models.CharField(max_length=32,
                              blank=True,
                              null=True)
    edad = models.IntegerField()
    email = models.CharField(max_length=32)

    def __str__(self):
        return self.nombre


class Clases(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True)
    nombre = models.CharField(max_length=30,
                              blank=True,
                              null=True)
    alumnos = models.ManyToManyField(Alumnos,
                                     related_name='alumnos',
                                     )

    def __str__(self):
        return self.nombre