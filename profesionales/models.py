from django.db import models

class Permanente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    area = models.CharField(max_length=40)
    desempleado = models.BooleanField()
    sueldo_aportes = models.IntegerField()
    
class Freelance(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    area = models.CharField(max_length=40)
    desempleado = models.BooleanField()
    tarea_asignada = models.CharField(max_length=35)
    fecha_entrega = models.DateTimeField(max_length=10)
    
class Administrativo(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    antigüedad = models.DateField(max_length=50)
    desempleado = models.BooleanField()
