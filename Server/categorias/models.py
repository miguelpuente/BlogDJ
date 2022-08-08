from django.db import models
from django.utils import timezone

# Creación de los atributos de la clase 'Categorias'
# Creación de los campos de la tabla 'categorias'

class Categorias(models.Model):
    nombre = models.CharField(max_length=150, default='DEFAULT VALUE')
    detalles = models.CharField(max_length=1500, default='DEFAULT VALUE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categorias'