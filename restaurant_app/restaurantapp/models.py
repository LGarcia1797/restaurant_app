from contextlib import nullcontext
from email.policy import default
from random import choices
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


estadoR = [(1, 'RESERVADO'), (2, 'COMPLETADO'), (3, 'ANULADO'), (4, 'NO ASISTEN')]


class reservas(models.Model):
    nombre=models.CharField(max_length=50)
    Npersonas=models.IntegerField(default=1, validators=[ MaxValueValidator(15), MinValueValidator(1)])
    telefono=models.IntegerField()
    diareserva=models.DateTimeField(auto_now_add=True)
    estado= models.IntegerField(
        null=False , blank=False,
        choices=estadoR,
        default=1
    )
    observacion=models.CharField(max_length=50,
        null=True, blank=True)



    

