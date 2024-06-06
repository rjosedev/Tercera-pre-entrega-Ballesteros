from django.shortcuts import render
from forms import ProveedorForm, DispositivoForm, SitioForm, BusquedaForm

def index(request):
    # Página principal
    return render(request, 'index.html', {})

def form_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProveedorForm()
    return render(request, 'form_proveedor.html', {'form': form})

def form_dispositivo(request):
    if request.method == 'POST':
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DispositivoForm()
    return render(request, 'form-dispositivo.html', {'form': form})

def form_sitio(request):
    if request.method == 'POST':
        form = SitioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SitioForm()
    return render(request, 'form-sitio.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino = form.cleaned_data['termino_busqueda']
            # Realiza la búsqueda en la base de datos según el término ingresado
            # y renderiza los resultados
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form})