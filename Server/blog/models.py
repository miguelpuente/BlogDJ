from django.db import models
from django.utils import timezone

# Creación de los atributos de la clase 'Blog'
# Creación de los campos de la tabla 'blogs'

class Blog(models.Model):
    detalles = models.CharField(max_length=5000, default='DEFAULT VALUE')
    logo = models.CharField(max_length=1000, default='DEFAULT VALUE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blogs'