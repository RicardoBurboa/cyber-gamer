from django.db import models

# Create your models here.

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(default='default.jpg', upload_to='img_juegos')
    descripcion = models.TextField()
    genero = models.CharField(default='No definido', max_length=20)
    multijugador = models.BooleanField(default=False)