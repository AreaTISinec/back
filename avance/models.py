from django.db import models
from obras.models import Obras
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Avances(models.Model):
    id_obra = models.ForeignKey(Obras, on_delete=models.CASCADE)
    fecha = models.DateField()
    porcentaje = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    tipo = models.CharField(max_length=255, null=False)
    nombre_hito = models.CharField(max_length=255, null=True, default='')