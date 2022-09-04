from django.db import models
from django.utils import timezone

# Creación de los atributos de la clase 'Posts'
# Creación de los campos de la tabla 'posts'

class Posts(models.Model):
    titulo = models.CharField(max_length=1000)
    contenido = models.TextField()
    visible = models.BooleanField(default=False)
    etiqueta = models.CharField(max_length=1000)
    imagen = models.CharField(max_length=1000)
    video = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'posts'