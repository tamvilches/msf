from django.contrib import admin
from .models import Rol, Region, Comuna, Medicamento, Receta, Persona, Usuario, Paciente, Cesfam, Despacho, Historial

# Register your models here.
admin.site.register(Rol)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Medicamento)
admin.site.register(Receta)
admin.site.register(Persona)
admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(Cesfam)
admin.site.register(Despacho)
admin.site.register(Historial)
