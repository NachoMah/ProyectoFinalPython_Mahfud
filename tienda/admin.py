from django.contrib import admin
from .models import Cliente, Producto, Empleado

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Empleado)