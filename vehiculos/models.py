from django.db import models

class Moto(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=30)
    fecha = models.DateField()
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"