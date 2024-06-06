from django.test import TestCase
from models import Proveedor, Dispositivo, Sitio

class ModelosTestCase(TestCase):
    def setUp(self):
        # Configurar datos de prueba
        self.proveedor = Proveedor.objects.create(nombre="Proveedor de Prueba")
        self.dispositivo = Dispositivo.objects.create(nombre="Dispositivo de Prueba", proveedor=self.proveedor)
        self.sitio = Sitio.objects.create(nombre="Sitio de Prueba", dispositivo=self.dispositivo)

    def test_proveedor(self):
        proveedor = Proveedor.objects.get(nombre="Proveedor de Prueba")
        self.assertEqual(proveedor.nombre, "Proveedor de Prueba")