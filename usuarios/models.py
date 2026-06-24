from django.db import models
from django.contrib.auth.models import AbstractUser




class UsuarioPersonalizado(AbstractUser):
    dni = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    email = models.EmailField(unique=True)
    def __str__(self):
        return f"{self.username} - {self.email}" 