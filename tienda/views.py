from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm, ProductoForm, EmpleadoForm, Producto, BuscarProductoFormulario
from .models import Producto, Publicacion

def listar_publicaciones(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha')
    return render(request, 'tienda/publicaciones.html', {'publicaciones': publicaciones})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'tienda/detalle_publicacion.html', {'publicacion': publicacion})

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