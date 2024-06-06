from django import forms
from AppCoder.models import Proveedor, Dispositivo, Sitio

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = '__all__'

class SitioForm(forms.ModelForm):
    class Meta:
        model = Sitio
        fields = '__all__'

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=100)