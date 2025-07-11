from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm, ProductoForm, EmpleadoForm, Producto, BuscarProductoFormulario, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Producto, Publicacion

def listar_publicaciones(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha')
    return render(request, 'tienda/publicaciones.html', {'publicaciones': publicaciones})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'tienda/detalle_publicacion.html', {'publicacion': publicacion})

def signup_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect('inicio')
    else:
        form = UserRegisterForm()
    return render(request, 'tienda/signup.html', {'form': form})

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
def perfil_view(request):
    return render(request, 'tienda/perfil.html')

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