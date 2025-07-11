from django.urls import path
from .views import inicio, crear_cliente, crear_producto, crear_empleado, buscar_producto, listar_publicaciones, detalle_publicacion, signup_view, login_view, logout_view, perfil_view

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('crear_cliente/', crear_cliente, name='crear_cliente'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('crear_empleado/', crear_empleado, name='crear_empleado'),
    path('buscar_producto/', buscar_producto, name='buscar_producto'),
    
    #Urls proyecto final
    
    path('pages/', listar_publicaciones, name='listar_publicaciones'),
    path('publicaciones/<int:pk>/', detalle_publicacion, name='detalle_publicacion'), 
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', perfil_view, name='perfil'), 
]