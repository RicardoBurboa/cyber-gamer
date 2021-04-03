from django.db import models

# Create your models here.

class Estacion(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(default='default.jpg', upload_to='img_estaciones')
    descripcion = models.TextField()