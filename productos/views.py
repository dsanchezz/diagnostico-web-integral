from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Producto
from .forms import ProductoForm


def lista_productos(request):
    """Vista para listar productos activos con búsqueda y paginación."""
    query = request.GET.get('q', '')
    productos_qs = Producto.objects.filter(activo=True)

    if query:
        productos_qs = productos_qs.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )

    paginator = Paginator(productos_qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
    }
    return render(request, 'productos/lista.html', context)


def detalle_producto(request, pk):
    """Vista para ver el detalle de un producto."""
    producto = get_object_or_404(Producto, pk=pk, activo=True)
    return render(request, 'productos/detalle.html', {'producto': producto})


def crear_producto(request):
    """Vista para crear un nuevo producto."""
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Producto creado exitosamente.')
            return redirect('productos:lista')
        else:
            messages.error(request, '❌ Por favor corrige los errores del formulario.')
    else:
        form = ProductoForm()

    return render(request, 'productos/formulario.html', {
        'form': form,
        'titulo': 'Nuevo Producto',
        'boton': 'Crear Producto',
    })


def editar_producto(request, pk):
    """Vista para editar un producto existente."""
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Producto actualizado exitosamente.')
            return redirect('productos:lista')
        else:
            messages.error(request, '❌ Por favor corrige los errores del formulario.')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'productos/formulario.html', {
        'form': form,
        'titulo': f'Editar: {producto.nombre}',
        'boton': 'Guardar Cambios',
        'producto': producto,
    })


def eliminar_producto(request, pk):
    """Vista para confirmar y realizar soft delete de un producto."""
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        producto.activo = False
        producto.save()
        messages.success(request, f'🗑️ Producto "{producto.nombre}" eliminado correctamente.')
        return redirect('productos:lista')

    return render(request, 'productos/confirmar_eliminar.html', {'producto': producto})
