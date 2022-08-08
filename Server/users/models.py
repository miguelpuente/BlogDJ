from django.db import models
from django.contrib.auth.models import AbstractUser

# Creación de los atributos de la clase 'Users'
# Creación de los campos de la tabla 'users'

class User(AbstractUser):
    """Extiende el usuario de django-- gracias django :)"""