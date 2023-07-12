from django.db import models

# Create your models here.
class Faccion(models.Model):
    nombre = models.CharField(max_length=50,unique=True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "Facción"
        verbose_name_plural = "Facciones"

class Personaje(models.Model):
    nombre = models.CharField(max_length=50,unique=True)
    faccion = models.ForeignKey(Faccion,on_delete=models.SET_NULL, null=True, blank=True)
    historia = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "Personaje"
        verbose_name_plural = "Personajes"