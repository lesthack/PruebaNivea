# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime

class Instrumento(models.Model):
    nombre = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return u'{} - {}'.format(self.id, self.nombre)

class Escala(models.Model):
    nombre = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return u'{}'.format(self.nombre)

    def getItems(self):
        return EscalaItem.objects.filter(escala=self).order_by('id')

class EscalaItem(models.Model):
    escala = models.ForeignKey(Escala, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)
    # agregar orden
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return u'{}: {}'.format(self.escala, self.nombre)

class Categoria(models.Model):
    nombre = models.CharField(max_length=250)
    orden = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return u'{}'.format(self.nombre)

class InstrumentoItem(models.Model):
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)
    pregunta = models.CharField(max_length=500)
    orden = models.IntegerField(default=0)
    escala = models.ForeignKey(Escala, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return u'{}: {}'.format(self.instrumento.nombre, self.pregunta)

class InstrumentoValor(models.Model):
    instrumento_item = models.ForeignKey(InstrumentoItem, on_delete=models.CASCADE)
    escala_item = models.ForeignKey(EscalaItem, on_delete=models.CASCADE)
    valor = models.IntegerField(default=0)

    def __str__(self):
        return u'{}'.format(self.id)

    def pregunta(self):
        return self.instrumento_item.pregunta
    pregunta.short_description = 'Pregunta'
    pregunta.allow_tags = True
    pregunta.admin_order_field = 'instrumento_item__orden'
    
    def nombre_categoria(self):
        return self.instrumento_item.categoria.nombre
    nombre_categoria.short_description = 'Categoria'
    nombre_categoria.allow_tags = True
    nombre_categoria.admin_order_field = 'instrumento_item.categoria.nombre'

    def nombre_escala(self):
        return self.escala_item.escala.nombre
    nombre_escala.short_description = 'Escala'
    nombre_escala.allow_tags = True
    nombre_escala.admin_order_field = 'escala_item.escala.nombre'

    def nombre_item(self):
        return self.escala_item.nombre
    nombre_item.short_description = 'Item'
    nombre_item.allow_tags = True
    nombre_item.admin_order_field = 'escala_item.nombre'

#class Aplicacion(models.Model):
#    GENERO_CHOICES = (
#        (0, 'Masculino'),
#        (1, 'Femenino')
#    )
#    ESCOLARIDAD_CHOICES = (
#        (0, 'Primaria'),
#        (1, 'Secundaria'),
#        (2, 'Preparatoria'),
#        (3, 'Universidad')
#    )
#    ESTADOCIVIL_CHOICES = (
#        (0, 'Soltero/a'),
#        (1, 'Casado/a'),
#        (2, 'Unión Libre'),
#        (3, 'Divorciado/a'),
#        (4, 'Separado/a'),
#        (5, 'Viudo/a'),
#    )
#    fecha = models.DateField(default=datetime.date.today)
#    edad = models.IntegerField() # Agregar validacion
#    sexo = models.IntegerField(choices=GENERO_CHOICES)
#    escolaridad = models.IntegerField(choices=ESCOLARIDAD_CHOICES)
#    estado_civil = models.IntegerField(choices=ESTADOCIVIL_CHOICES)
#    puesto = models.CharField(max_length=500)
#    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
#    created_at = models.DateTimeField(auto_now_add = True)
#    updated_at = models.DateTimeField(auto_now = True)
#    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return 'Aplicacion {}'.format(self.id)
#
#class AplicacionItem(models.Model):
#    aplicacion = models.ForeignKey(Aplicacion, on_delete=models.CASCADE)
#    item = models.ForeignKey(InstrumentoItem, on_delete=models.CASCADE)
#    respuesta = models.IntegerField(default=-1)
#    created_at = models.DateTimeField(auto_now_add = True)
#    updated_at = models.DateTimeField(auto_now = True)
#    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#
#    def __unicode__(self):
#        return '{}. {}: {}'.format(self.item.instrumento.nombre, self.item.pregunta, self.respuesta)
