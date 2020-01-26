from django.db import models
from django.contrib.auth.models import User
import datetime

class Instrumento(models.Model):
    nombre = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.id, self.nombre)

class Escala(models.Model):
    nombre = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '{}'.format(self.nombre)

class EscalaItem(models.Model):
    escala = models.ForeignKey(Escala, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)
    valor = models.IntegerField(default=-1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '{}: {}'.format(self.escala, self.nombre)

class InstrumentoItem(models.Model):
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=500)
    descripcion = models.TextField()
    escala = models.ForeignKey(Escala, on_delete=models.CASCADE)
    grupo = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.instrumento.nombre, self.pregunta)

class Aplicacion(models.Model):
    GENERO_CHOICES = (
        (0, 'Masculino'),
        (1, 'Femenino')
    )
    ESCOLARIDAD_CHOICES = (
        (0, 'Primaria'),
        (1, 'Secundaria'),
        (2, 'Preparatoria'),
        (3, 'Universidad')
    )
    ESTADOCIVIL_CHOICES = (
        (0, 'Soltero/a'),
        (1, 'Casado/a'),
        (2, 'Unión Libre'),
        (3, 'Divorciado/a'),
        (4, 'Separado/a'),
        (5, 'Viudo/a'),
    )
    fecha = models.DateField(default=datetime.date.today)
    edad = models.IntegerField() # Agregar validacion
    sexo = models.IntegerField(choices=GENERO_CHOICES)
    escolaridad = models.IntegerField(choices=ESCOLARIDAD_CHOICES)
    estado_civil = models.IntegerField(choices=ESTADOCIVIL_CHOICES)
    puesto = models.CharField(max_length=500)
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Aplicacion {}'.format(self.id)

class AplicacionItem(models.Model):
    item = models.ForeignKey(InstrumentoItem, on_delete=models.CASCADE)
    respuesta = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return '{}. {}: {}'.format(self.item.instrumento.nombre, self.item.pregunta, self.respuesta)
