from django.contrib import admin
from .models import Cliente, Producto, Empleado, Publicacion

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Empleado)
admin.site.register(Publicacion)