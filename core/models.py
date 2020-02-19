# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.html import format_html
import datetime

class Escala(models.Model):
    nombre = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return u'{}'.format(self.nombre)

    def getItems(self):
        return EscalaItem.objects.filter(escala=self).order_by('id')

    def go_items(self):
        return format_html('<a href="/admin/core/escalaitem/?escala__nombre={}">Ver</a>', self.nombre)
    go_items.short_description = 'Items'
    go_items.allow_tags = False

class EscalaItem(models.Model):
    escala = models.ForeignKey(Escala, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)
    # agregar orden
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return u'{}: {}'.format(self.escala, self.nombre)

    def nombre_escala(self):
        return self.escala.nombre
    nombre_escala.short_description = 'Escala'
    nombre_escala.allow_tags = True
    nombre_escala.admin_order_field = 'escala__nombre'

class Localidad(models.Model):
    nombre = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '{}'.format(self.nombre)

class Competencia(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    apto = models.TextField()
    apto_min = models.IntegerField(default=0)
    apto_max = models.IntegerField(default=0)
    apto_condicionado = models.TextField()
    apto_condicionado_min = models.IntegerField(default=0)
    apto_condicionado_max = models.IntegerField(default=0)
    no_apto = models.TextField()
    no_apto_min = models.IntegerField(default=0)
    no_apto_max = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return u'{}'.format(self.nombre)

class Conducta(models.Model):
    competencia = models.ManyToManyField(Competencia)
    pregunta = models.CharField(max_length=500)
    orden = models.IntegerField(default=0)
    escala = models.ForeignKey(Escala, on_delete=models.CASCADE)
    invertido = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.pregunta

class ConductaValor(models.Model):
    conducta = models.ForeignKey(Conducta, on_delete=models.CASCADE)
    escala_item = models.ForeignKey(EscalaItem, on_delete=models.CASCADE)
    valor = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return u'{}'.format(self.id)

    def pregunta(self):
        return self.conducta.pregunta
    pregunta.short_description = 'Pregunta'
    pregunta.allow_tags = True
    pregunta.admin_order_field = 'conducta__orden'
    
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

class Evaluacion(models.Model):
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
    NUMEROHIJOS_CHOICES = (
        (0, 'Ninguno'),
        (1,'Uno'),
        (2,'Dos'),
        (3,'Tres'),
        (4,'Cuatro'),
        (5,'Cinco'),
        (6,'Seis o mas')
    )
    nombre_persona = models.CharField(max_length=250)
    fecha = models.DateField(default=datetime.date.today)
    edad = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(60)])
    sexo = models.IntegerField(choices=GENERO_CHOICES)
    estado_civil = models.IntegerField(choices=ESTADOCIVIL_CHOICES)
    escolaridad = models.IntegerField(choices=ESCOLARIDAD_CHOICES)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    numero_hijos = models.IntegerField(choices=NUMEROHIJOS_CHOICES)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Evaluacion {}'.format(self.id)

    def get_sexo(self):
        return '{}'.format(self.GENERO_CHOICES[self.sexo][1])

    def get_escolaridad(self):
        return '{}'.format(self.ESCOLARIDAD_CHOICES[self.escolaridad][1])

    def get_estado_civil(self):
        return '{}'.format(self.ESTADOCIVIL_CHOICES[self.estado_civil][1])

    def get_numero_hijos(self):
        return '{}'.format(self.NUMEROHIJOS_CHOICES[self.numero_hijos][1])

class EvaluacionRespuesta(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    conducta = models.ForeignKey(Conducta, on_delete=models.CASCADE)
    respuesta = models.IntegerField(default=-1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.respuesta) 
