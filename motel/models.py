from django.db import models

class Distrito(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Motel(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    horario = models.CharField(max_length=15, null=True, blank=True)
    tarifa = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre