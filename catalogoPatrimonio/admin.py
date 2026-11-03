from django.contrib import admin
from .models import Categoria, LugarPatrimonial

# Register your models here.

# Registro simple de categoria
admin.site.register(Categoria)

# Registro personalizado para LugarPatrimonial
class LugarPatrimonialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'anio_construccion')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'ubicacion')

admin.site.register(LugarPatrimonial, LugarPatrimonialAdmin)