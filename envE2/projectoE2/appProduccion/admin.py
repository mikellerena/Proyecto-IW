from django.contrib import admin
from .models import Equipo, Empleado, Proceso, Novedades

# Register your models here.
admin.site.register(Equipo)
admin.site.register(Empleado)
admin.site.register(Proceso)
admin.site.register(Novedades)
