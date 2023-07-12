from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Faccion)
admin.site.register(models.Personaje)