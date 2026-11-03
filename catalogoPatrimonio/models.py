from django.db import models

# Create your models here.

# Modelo 1: Categoria (Contiene: id, nombre, descripcion)
#NOTA: el id es asignado automaticamente por Django

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo 2: LugarPatrimonial (Contiene: id, nombre, descripcion, ubicacion, anio_construccion, imagen, categoria (FK))

class LugarPatrimonial(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    anio_construccion = models.IntegerField()
    # Se usan URL para las imagenes, asi el renderizado es mas rapido y no requerimos alojamiento local de ellas. Tal como se propone en el documento.
    imagen = models.URLField(max_length=300)
    # Relacion 1:N con categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre