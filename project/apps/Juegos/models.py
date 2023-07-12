from django.db import models

# Create your models here.

class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    direccion_url = models.CharField(max_length=100,unique=True)
    descripcion = models.TextField(max_length=250)

    def __str__(self) -> str:
        return self.nombre