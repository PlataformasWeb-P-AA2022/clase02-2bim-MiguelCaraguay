from django.contrib import admin

# Register your models here.
from mundial.models import Estadio, Equipo
admin.site.register(Estadio)
admin.site.register(Equipo)