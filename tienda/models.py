from django.db import models
from ckeditor.fields import RichTextField

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='publicaciones/')
    fecha = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo

#Modelos tercer entregable

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    informacion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nombre
    
    
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.puesto})"