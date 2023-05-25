from django.db import models

# Create your models here.
class Resultado(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
