from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm, ProductoForm, EmpleadoForm, Producto, BuscarProductoFormulario, RegistroUsuarioForm, EditarPerfilForm, ContactoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Producto, Publicacion, Perfil

def listar_publicaciones(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha')
    return render(request, 'tienda/publicaciones.html', {'publicaciones': publicaciones})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'tienda/detalle_publicacion.html', {'publicacion': publicacion})

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, "Hubo un error en el formulario. Revisá los datos.")
    else:
        form = RegistroUsuarioForm()
    return render(request, 'tienda/registro.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Has iniciado sesión correctamente.")
            return redirect('inicio')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'tienda/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión.")
    return redirect('inicio')

@login_required
def ver_perfil(request):
    perfil = request.user.perfil
    return render(request, 'tienda/perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    perfil = request.user.perfil
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=perfil, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('ver_perfil')
    else:
        form = EditarPerfilForm(instance=perfil, user=request.user)
    return render(request, 'tienda/editar_perfil.html', {'form': form})

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Podrías guardar o procesar los datos, pero en este caso no es necesario
            messages.success(request, "Gracias por tu mensaje. ¡Te responderemos pronto!")
            return redirect('contacto')
    else:
        form = ContactoForm()
    return render(request, 'tienda/contacto.html', {'form': form})

#Vistas tercer entregable:

def inicio(request):
    return render(request,'tienda/inicio.html')

def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  
    else:
        form = ClienteForm()
    return render(request, 'tienda/cliente.html', {'form': form})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  
    else:
        form = ProductoForm()
    return render(request, 'tienda/producto.html', {'form': form})


def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio') 
    else:
        form = EmpleadoForm()
    return render(request, 'tienda/empleado.html', {'form': form})

def buscar_producto(request):
    form = BuscarProductoFormulario()
    resultados = []
    busqueda_realizada = False           
    if request.method == "GET" and "nombre" in request.GET:
        form = BuscarProductoFormulario(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            resultados = Producto.objects.filter(nombre__icontains=nombre)
            busqueda_realizada = True    
    return render(
        request,
        'tienda/buscar_producto.html',
        {
            'form': form,
            'resultados': resultados,
            'busqueda_realizada': busqueda_realizada,  
        },
    )