from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogoPatrimonio/', views.catalogo_view, name='catalogo'),
    path('lugar/<int:id>/', views.detalle_lugar, name='detalle'),
]