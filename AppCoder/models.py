from django.db import models

# Modelos: Proveedor, Dispositivo y Sitio

class Proveedor(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    telefono = models.IntegerField()
    referente = models.CharField(max_length=30)
    num_id = models.IntegerField()
    
class Dispositivo(models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    proveedor = models.CharField(max_length=20)
    rack = models.CharField(max_length=20)
    sitio = models.CharField(max_length=20)
    num_id = models.IntegerField()

class Sitio(models.Model):
    nombre = models.CharField(max_length=20)
    dirección = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    switchowner = models.CharField(max_length=30)
    num_id = models.IntegerField()