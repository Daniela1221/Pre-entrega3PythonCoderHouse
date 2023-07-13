from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.ObraCinematográfica)
admin.site.register(models.TipoCinematográfico)
