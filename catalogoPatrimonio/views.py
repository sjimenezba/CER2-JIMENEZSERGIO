from django.shortcuts import render, get_object_or_404
from .models import LugarPatrimonial, Categoria
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import LugarForm

# Create your views here.
# RF01: Principal, presentacion de la fundacion y acceso
def index(request):
    return render(request, 'catalogo/index.html')

# RF02: Listado de lugares registrados
def catalogo_view(request):
    lugares = LugarPatrimonial.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'catalogo/catalogo.html', {'lugares': lugares, 'categorias': categorias})
#RF05
def filtro_categoria(request, id):
    categoria_seleccionada = get_object_or_404(Categoria, id=id)
    lugares = LugarPatrimonial.objects.filter(categoria=categoria_seleccionada)
    categorias = Categoria.objects.all()

    return render(request, 'catalogo/catalogo.html', {
        'lugares': lugares,
        'categorias': categorias,
        'categoria_seleccionada': categoria_seleccionada
    })

#RF03: Vista individual con la info del lugar
def detalle_lugar(request, id):
    lugar = get_object_or_404(LugarPatrimonial, id=id)
    return render(request, 'catalogo/detalle.html', {'lugar': lugar})

#RF10
@login_required
def gestion_patrimonial(request):
    lugares = LugarPatrimonial.objects.all()
    return render(request, 'catalogo/gestion.html', {'lugares': lugares})

#RF11 y RF12, agregar lugar + permisos
@permission_required('catalogoPatrimonio.add_lugarpatrimonial', raise_exception=True)
def agregar_lugar(request):
    if request.method == 'POST':
        form = LugarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion')
    else:
        form = LugarForm()

    return render(request, 'catalogo/lugar_form.html', {'form': form, 'accion': 'Agregar'})

#RF11 y RF12, modificar lugar + permisos
@permission_required('catalogoPatrimonio.change_lugarpatrimonial', raise_exception=True)
def editar_lugar(request, id):
    lugar = get_object_or_404(LugarPatrimonial, id=id)

    if request.method == 'POST':
        form = LugarForm(request.POST, instance=lugar)
        if form.is_valid():
            form.save()
            return redirect('gestion')
    else:
        form = LugarForm(instance=lugar)

    return render(request, 'catalogo/lugar_form.html', {'form': form, 'accion': 'Editar'})