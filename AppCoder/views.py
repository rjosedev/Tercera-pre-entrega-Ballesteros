from django.shortcuts import render
from django.template import loader
from .forms import ProveedorForm, DispositivoForm, SitioForm, BusquedaForm
from .models import Proveedor, Dispositivo, Sitio
from http import HTTPMethod
from django.http import HttpRequest

def index(request):
    # Página principal
    return render(request, 'AppCoder/index.html', {})

def form_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProveedorForm()
    return render(request, 'AppCoder/agregar-proveedor.html', {'form': form})

def form_dispositivo(request):
    if request.method == 'POST':
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DispositivoForm()
    return render(request, 'AppCoder/agregar-dispositivo.html', {'form': form})

def form_sitio(request):
    if request.method == 'POST':
        form = SitioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SitioForm()
    return render(request, 'AppCoder/agregar-sitio.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino = form.cleaned_data['termino_busqueda']
            # Realiza la búsqueda en la base de datos según el término ingresado
            # y renderiza los resultados
    else:
        form = BusquedaForm()
    return render(request, 'AppCoder/buscar.html', {'form': form})

def list_proveedor(request):
    lista = Proveedor.objects.all()
    return render(request, 'AppCoder/listar-proveedor.html', {'lista-proveedores': lista})

def list_dispositivo(request):
    lista = Dispositivo.objects.all()
    return render(request, 'AppCoder/listar-dispositivo.html', {'lista-dispositivos': lista})

def list_sitio(request):
    lista = Sitio.objects.all()
    return render(request, 'AppCoder/listar-sitio.html', {'lista-sitios': lista})