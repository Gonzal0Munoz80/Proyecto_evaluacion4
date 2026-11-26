from django.db import models

# Create your models here.
class eventos(models.Model):
    nombre = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    descripcion = models.TextField()
    valor = models.DecimalField(help_text="Valor de la entrada en pesos")
    cupos = models.PositiveBigIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def cupos_disponibles(self):
        ocupados = sum(i.cantidad for i in self.inscripciones.all())
        return self.cupos - ocupados


class inscripciones(models.Model):
    evento = models.ForeignKey(eventos,on_delete=models.CASCADE, related_name='inscripciones')
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    cantidad = models.PositiveIntegerField(default=1)
    creada = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.nombre} - {self.evento}"
    