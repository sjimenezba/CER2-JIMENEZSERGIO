from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogoPatrimonio/', views.catalogo_view, name='catalogo'),
    path('lugar/<int:id>/', views.detalle_lugar, name='detalle'),
    path('categoria/<int:id>/', views.filtro_categoria, name='filtro'),

    #Rutas nuevas de RF10, 11 y 12
    path('gestion/', views.gestion_patrimonial, name='gestion'),
    path('gestion/agregar/', views.agregar_lugar, name='agregar_lugar'),
    path('gestion/editar/<int:id>/', views.editar_lugar, name='editar_lugar'),
]