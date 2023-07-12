from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Libreria)
admin.site.register(models.TipoLiteratura)