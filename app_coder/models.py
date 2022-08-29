from django.db import models

# Estudiantes (nombre, apellido, email)
# Profesor (nombre, apellido, email, profesión)
# Entregable (nombre, fechaDeEntrega,entregado)
# Curso (nombre, comisión)"

# Create your models here.

class Estudiante (models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()
    pass

class Profesor (models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()
    profesion = models.CharField(max_length=64)
    pass

class Curso (models.Model):
    nombre = models.CharField(max_length=128)
    comision = models.IntegerField()
    pass

class Entregable (models.Model):
    nombre = models.CharField(max_length=128)
    entregado = models.BooleanField()
    fecha_entrega = models.DateField()
    pass
