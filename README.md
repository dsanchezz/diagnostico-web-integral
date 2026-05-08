# Tienda Django — CRUD de Productos

Sistema web de gestión de productos desarrollado con Django y SQLite. Permite administrar un catálogo de productos con operaciones completas de creación, lectura, actualización y eliminación desde una interfaz moderna y responsiva.

---

## Tecnologías utilizadas

| Capa | Tecnología |
|---|---|
| Backend | Python 3.x + Django 6.0 |
| Base de datos | SQLite 3 (default) / MySQL 8.x (opcional) |
| ORM | Django ORM |
| Frontend | HTML5 + Tailwind CSS (CDN) |
| Panel de administración | Django Admin |

---

---

## Estructura del proyecto

```
tienda/
├── manage.py
├── seed_data.py
├── db.sqlite3
├── requirements.txt
├── tienda/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── productos/
│   ├── management/
│   │   └── commands/
│   │       └── seed_data.py
│   ├── migrations/
│   ├── templates/
│   │   └── productos/
│   │       ├── lista.html
│   │       ├── detalle.html
│   │       ├── formulario.html
│   │       └── confirmar_eliminar.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── templates/
    └── base.html
```

---

## Instrucciones para ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tienda-django.git
cd tienda-django
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Cargar datos de prueba

```bash
python manage.py seed_data
```

Esto crea 5 categorías (Electrónica, Ropa, Hogar, Deportes, Alimentos) y 12 productos de ejemplo.

### 6. Crear un superusuario (para el panel admin)

```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

La aplicación estará disponible en:

- **Productos:** http://localhost:8000/
- **Admin:** http://localhost:8000/admin/

---

## Base de datos alternativa (MySQL)

Por defecto el proyecto usa SQLite. Para usar MySQL, edita `tienda/settings.py` y reemplaza el bloque `DATABASES`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tienda_db',
        'USER': 'root',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Luego crea la base de datos en MySQL:

```sql
CREATE DATABASE tienda_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

---

## Modelo de datos

### Producto

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | AutoField | Clave primaria |
| `nombre` | CharField(200) | Nombre del producto |
| `descripcion` | TextField | Descripción opcional |
| `precio` | DecimalField | Precio con 2 decimales |
| `stock` | PositiveIntegerField | Unidades disponibles |
| `categoria` | ForeignKey | Relación con Categoria |
| `activo` | BooleanField | Soft delete flag |
| `creado_en` | DateTimeField | Fecha de creación automática |

### Categoria

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | AutoField | Clave primaria |
| `nombre` | CharField(100) | Nombre de la categoría |

---

## Rutas disponibles

| Método | URL | Acción |
|---|---|---|
| GET | `/` | Redirige a la lista de productos |
| GET | `/productos/` | Listar todos los productos activos |
| GET | `/productos/<id>/` | Ver detalle de un producto |
| GET / POST | `/productos/nuevo/` | Crear un nuevo producto |
| GET / POST | `/productos/<id>/editar/` | Editar un producto existente |
| GET / POST | `/productos/<id>/eliminar/` | Confirmar y eliminar producto |
