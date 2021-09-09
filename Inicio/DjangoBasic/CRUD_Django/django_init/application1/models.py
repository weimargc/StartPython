from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 120)
    correo = models.EmailField(max_length = 200)