from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Departamentos(models.Model):
    nombre = models.CharField(max_length=20)
    longitud = models.FloatField()
    latitud = models.FloatField()

    def ubicacion(self):
        return self.longitud+" "+self.latitud
