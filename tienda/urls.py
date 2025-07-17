from django.urls import path
from .views import inicio, crear_cliente, crear_producto, crear_empleado, buscar_producto, detalle_publicacion, registro_usuario, login_view, logout_view, ver_perfil, editar_perfil, contacto, about, registros, PublicacionListView, PublicacionCreateView, PublicacionUpdateView, PublicacionDeleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('crear_cliente/', crear_cliente, name='crear_cliente'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('crear_empleado/', crear_empleado, name='crear_empleado'),
    path('buscar_producto/', buscar_producto, name='buscar_producto'),
    #Urls proyecto final
    
    path('pages/', PublicacionListView.as_view(), name='listar_publicaciones'),
    path('pages/crear/', PublicacionCreateView.as_view(), name='crear_publicacion'),
    path('publicaciones/<int:pk>/', detalle_publicacion, name='detalle_publicacion'), 
    path('registro/', registro_usuario, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', ver_perfil, name='ver_perfil'), 
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/cambiar-password/', auth_views.PasswordChangeView.as_view(template_name='tienda/cambiar_password.html'), name='password_change'),
    path('perfil/password-ok/', auth_views.PasswordChangeDoneView.as_view(template_name='tienda/password_ok.html'), name='password_change_done'),
    path('contacto/', contacto, name='contacto'),
    path('about/', about, name='about'),
    path('publicaciones/<int:pk>/editar/', PublicacionUpdateView.as_view(), name='editar_publicacion'),
    path('publicaciones/<int:pk>/eliminar/', PublicacionDeleteView.as_view(), name='eliminar_publicacion'),
    path('registros/', registros, name='registros'),
    ]