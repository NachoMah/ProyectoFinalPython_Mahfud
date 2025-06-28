from django.shortcuts import render, redirect
from .forms import ClienteForm, ProductoForm, EmpleadoForm

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
            return redirect('inicio')  # ✅ redirige al inicio
    else:
        form = EmpleadoForm()
    return render(request, 'tienda/empleado.html', {'form': form})