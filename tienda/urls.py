from django.urls import path
from .views import inicio, crear_cliente, crear_producto, crear_empleado, buscar_producto, listar_publicaciones, detalle_publicacion

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('crear_cliente/', crear_cliente, name='crear_cliente'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('crear_empleado/', crear_empleado, name='crear_empleado'),
    path('buscar_producto/', buscar_producto, name='buscar_producto'),
    
    #Urls proyecto final
    
    path('pages/', listar_publicaciones, name='listar_publicaciones'),
    path('publicaciones/<int:pk>/', detalle_publicacion, name='detalle_publicacion'),  
]