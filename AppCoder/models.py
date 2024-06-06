from django.db import models

# Modelos: Padre, Proveedor, Dispositivo y Sitio

class Padre(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    num_id = models.IntegerField()
    class Meta:
        abstract = True

class Proveedor(Padre, models.Model):
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    referente = models.CharField(max_length=100)
    
class Dispositivo(Padre, models.Model):
    tipo = models.CharField(max_length=100)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    rack = models.CharField(max_length=100)
    sitio = models.CharField(max_length=100)

class Sitio(Padre, models.Model):
    switchowner = models.CharField(max_length=100)