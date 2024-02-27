from django.db import models
from django.conf import settings

from empresas.models import Empresa
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, default='')
    apellido = models.CharField(max_length=255, default='')
    numero = models.CharField(max_length=255, default='')
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'