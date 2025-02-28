from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=64)
    apellidos = models.CharField(max_length=64)
    rfc = models.CharField(max_length=15, unique=True)
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=True)  #Nota: He corregido BoolField por BooleanField que es el correcto en Django.
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"