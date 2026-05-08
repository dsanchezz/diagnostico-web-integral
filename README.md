# 🛍️ Tienda Django — CRUD de Productos

Sistema web de gestión de productos desarrollado con Django y MySQL. Permite administrar un catálogo de productos con operaciones completas de creación, lectura, actualización y eliminación desde una interfaz moderna y responsiva.

---

## 🛠️ Tecnologías utilizadas

| Capa | Tecnología |
|---|---|
| Backend | Python 3.11 + Django 4.x |
| Base de datos | MySQL 8.x |
| ORM | Django ORM |
| Frontend | HTML5 + Tailwind CSS (CDN) |
| Subida de archivos | Django + Pillow |
| Panel de administración | Django Admin |

---

## ✨ Funcionalidades

- **Listar productos** — vista en tarjetas con imagen, precio y stock
- **Crear producto** — formulario con validación del lado del servidor
- **Editar producto** — formulario prellenado con los datos actuales
- **Eliminar producto** — soft delete (se marca como inactivo, no se borra físicamente)
- **Búsqueda** — filtrado por nombre o descripción en tiempo real
- **Paginación** — 10 productos por página
- **Categorías** — relación ForeignKey con modelo Categoria
- **Subida de imágenes** — imagen opcional por producto
- **Mensajes de confirmación** — notificaciones de éxito y error tras cada acción
- **Panel de administración** — gestión avanzada desde `/admin/`

---

## 📁 Estructura del proyecto

```
tienda/
├── manage.py
├── tienda/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── productos/
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
├── templates/
│   └── base.html
├── media/
│   └── productos/
└── requirements.txt
```

---

## ⚙️ Instrucciones para ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tienda-django.git
cd tienda-django
```

### 2. Crear y activar el entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar en Linux / macOS
source venv/bin/activate

# Activar en Windows
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

Contenido de `requirements.txt`:

```
django>=4.2
mysqlclient>=2.1
pillow>=10.0
```

### 4. Crear la base de datos en MySQL

Conéctate a MySQL y ejecuta:

```sql
CREATE DATABASE tienda_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 5. Configurar la conexión a la base de datos

Edita `tienda/settings.py` con tus credenciales:

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

### 6. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crear un superusuario (para el panel admin)

```bash
python manage.py createsuperuser
```

### 8. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

La aplicación estará disponible en:

- **Productos:** http://localhost:8000/productos/
- **Admin:** http://localhost:8000/admin/

---

## 🗄️ Modelo de datos

### Producto

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | AutoField | Clave primaria |
| `nombre` | CharField(200) | Nombre del producto |
| `descripcion` | TextField | Descripción opcional |
| `precio` | DecimalField | Precio con 2 decimales |
| `stock` | PositiveIntegerField | Unidades disponibles |
| `categoria` | ForeignKey | Relación con Categoria |
| `imagen` | ImageField | Foto del producto (opcional) |
| `activo` | BooleanField | Soft delete flag |
| `creado_en` | DateTimeField | Fecha de creación automática |

### Categoria

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | AutoField | Clave primaria |
| `nombre` | CharField(100) | Nombre de la categoría |

---

## 🔗 Rutas disponibles

| Método | URL | Acción |
|---|---|---|
| GET | `/productos/` | Listar todos los productos |
| GET | `/productos/<id>/` | Ver detalle de un producto |
| GET / POST | `/productos/nuevo/` | Crear un nuevo producto |
| GET / POST | `/productos/<id>/editar/` | Editar un producto existente |
| GET / POST | `/productos/<id>/eliminar/` | Confirmar y eliminar producto |

---


