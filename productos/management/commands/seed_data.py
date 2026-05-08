from django.core.management.base import BaseCommand
from productos.models import Categoria, Producto


class Command(BaseCommand):
    help = 'Carga datos de prueba: categorías y productos'

    def handle(self, *args, **kwargs):
        categorias_data = ['Electrónica', 'Ropa', 'Hogar', 'Deportes', 'Alimentos']
        categorias = {}
        for nombre in categorias_data:
            cat, created = Categoria.objects.get_or_create(nombre=nombre)
            categorias[nombre] = cat
            status = '✅ Creada' if created else '⏭️  Ya existe'
            self.stdout.write(f'{status}: {nombre}')

        productos_data = [
            {'nombre': 'Laptop Dell XPS 15', 'descripcion': 'Laptop ultradelgada con pantalla 4K OLED, procesador Intel i7 de última generación y 16GB RAM.', 'precio': 25000.00, 'stock': 5, 'categoria': 'Electrónica'},
            {'nombre': 'Camiseta Nike Dri-FIT', 'descripcion': 'Camiseta deportiva con tecnología de absorción de humedad, perfecta para entrenamiento.', 'precio': 450.00, 'stock': 12, 'categoria': 'Ropa'},
            {'nombre': 'Lámpara LED Inteligente', 'descripcion': 'Lámpara RGB controlable por WiFi con 16 millones de colores y temporizador.', 'precio': 1200.00, 'stock': 3, 'categoria': 'Hogar'},
            {'nombre': 'Audífonos Sony WH-1000XM5', 'descripcion': 'Audífonos inalámbricos con cancelación de ruido líder en la industria y 30 horas de batería.', 'precio': 6500.00, 'stock': 8, 'categoria': 'Electrónica'},
            {'nombre': 'Balón Adidas Champions League', 'descripcion': 'Balón oficial de la Champions League, tamaño 5, cosido a máquina.', 'precio': 890.00, 'stock': 15, 'categoria': 'Deportes'},
            {'nombre': 'Café Oaxaqueño Premium', 'descripcion': 'Café de altura 100% arábica, tostado medio, origen Pluma Hidalgo, Oaxaca. 500g.', 'precio': 320.00, 'stock': 25, 'categoria': 'Alimentos'},
            {'nombre': 'Sudadera Hoodie Oversize', 'descripcion': 'Sudadera unisex de algodón premium con capucha y bolsillo canguro.', 'precio': 680.00, 'stock': 20, 'categoria': 'Ropa'},
            {'nombre': 'Smart TV Samsung 55"', 'descripcion': 'Televisor 4K UHD con tecnología Crystal, HDR10+ y sistema operativo Tizen.', 'precio': 12999.00, 'stock': 4, 'categoria': 'Electrónica'},
            {'nombre': 'Set de Sartenes Antiadherentes', 'descripcion': 'Juego de 3 sartenes de cerámica antiadherente, libres de PFOA. Incluye 20cm, 24cm y 28cm.', 'precio': 1450.00, 'stock': 10, 'categoria': 'Hogar'},
            {'nombre': 'Mancuernas Ajustables 20kg', 'descripcion': 'Par de mancuernas ajustables de 2 a 20kg cada una, perfectas para home gym.', 'precio': 2800.00, 'stock': 6, 'categoria': 'Deportes'},
            {'nombre': 'Teclado Mecánico Logitech G Pro', 'descripcion': 'Teclado mecánico TKL con switches GX Blue, iluminación RGB LIGHTSYNC.', 'precio': 2200.00, 'stock': 7, 'categoria': 'Electrónica'},
            {'nombre': 'Proteína Whey Gold Standard', 'descripcion': 'Proteína de suero de leche, 2.27kg, sabor chocolate doble. 24g de proteína por servicio.', 'precio': 1350.00, 'stock': 18, 'categoria': 'Alimentos'},
        ]

        for data in productos_data:
            categoria = categorias[data.pop('categoria')]
            producto, created = Producto.objects.get_or_create(
                nombre=data['nombre'],
                defaults={**data, 'categoria': categoria}
            )
            status = '✅ Creado' if created else '⏭️  Ya existe'
            self.stdout.write(f'{status}: {producto.nombre}')

        self.stdout.write(self.style.SUCCESS(
            f'\n🎉 Seed completado: {Categoria.objects.count()} categorías, {Producto.objects.count()} productos'
        ))
