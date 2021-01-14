# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.html import format_html
from django.db.models import Sum, Max
import datetime
import math

COLORS = {
  'primary': {
    # nivel: color
    0: '#008000',
    2: '#ffff00',
    3: '#ff0000',
  },
  'secondary': {
    # nivel: color
    0: '#92D050',
    2: '#F19D65',
    3: '#FF2828',
  },
}

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
    tipo = models.SmallIntegerField(default=0)
    contra_titulo = models.CharField(max_length=250, default='')
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return u'{}'.format(self.nombre)

    def get_sum_total(self):
        _sum_ = Conducta.objects.filter(competencia=self) \
            .values('id') \
            .annotate(v=Max('conductavalor__valor')) \
            .aggregate(Sum('v'))
        return _sum_['v__sum']

    def get_escala(self):
        escala = {}
        # No Apto
        m = self.no_apto_max - self.no_apto_min
        for i in range(0,25):
            v = 100-i
            if v == 100: escala[v] = self.no_apto_max
            else: escala[v] = escala[v+1] - (m/25) 
        # Apto Condicionado
        m = self.apto_condicionado_max - self.apto_condicionado_min
        for i in range(0,25):
            v = 75-i
            escala[v] = escala[v+1] - (m/25) 
        # Apto
        m = self.apto_max - self.apto_min
        for i in range(0,50):
            v = 50-i
            escala[v] = escala[v+1] - (m/50) 
        return escala

    def get_barras(self, val):
        values = {
            'apto': 0,
            'apto_condicionado': 0,
            'no_apto': 0,
            'total': 0
        }
        escala = self.get_escala()
        if val >= self.apto_max:
            values['apto'] = 50
            if val >= self.apto_condicionado_max:
                values['apto_condicionado'] = 75-50
                if val >= self.no_apto_max:
                    values['no_apto'] = 100-75
                else:
                    for p in escala:
                        if val >= escala[p]:
                            values['no_apto'] = (0, p-75)[p-75>0]
                            break
            else:
                for p in escala:
                    if val >= escala[p]:
                        values['apto_condicionado'] = (0, p-50)[p-50>0]
                        break
        else:
            for p in escala:
                if val >= escala[p]:
                    values['apto'] = p
                    break
        values['total'] = values['apto'] + values['apto_condicionado'] + values['no_apto']
        return values

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
        (-1, 'No Definido'),
        (0, 'Masculino'),
        (1, 'Femenino')
    )
    ESCOLARIDAD_CHOICES = (
        (-1, 'No Definido'),
        (0, 'Primaria'),
        (1, 'Secundaria'),
        (2, 'Preparatoria'),
        (3, 'Universidad'),
        (4, 'Carrera Técnica')
    )
    ESTADOCIVIL_CHOICES = (
        (-1, 'No Definido'),
        (0, 'Soltero/a'),
        (1, 'Casado/a'),
        (2, 'Unión Libre'),
        (3, 'Divorciado/a'),
        (4, 'Separado/a'),
        (5, 'Viudo/a'),
    )
    NUMEROHIJOS_CHOICES = (
        (-1, 'No Definido'),
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
    fecha_nacimiento = models.DateField(null=True, blank=True)
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

    def save(self, *args, **kwargs):
        self.edad = -1
        self.sexo = -1
        self.estado_civil = -1
        self.escolaridad = -1
        self.localidad_id = -1
        self.numero_hijos = -1
        super(Evaluacion, self).save(*args, **kwargs)

    def get_sexo(self):
        return '{}'.format(self.GENERO_CHOICES[self.sexo][1])
    
    def get_sexo_abr(self):
        return '{}'.format(self.GENERO_CHOICES[self.sexo][1][0])

    def get_escolaridad(self):
        return '{}'.format(self.ESCOLARIDAD_CHOICES[self.escolaridad][1])

    def get_estado_civil(self):
        return '{}'.format(self.ESTADOCIVIL_CHOICES[self.estado_civil][1])

    def get_numero_hijos(self):
        return '{}'.format(self.NUMEROHIJOS_CHOICES[self.numero_hijos][1])

    def get_calificacion(self, competencia=None):
        total = 0
        porciento = 0
        inverso = 0
        calificacion = {
        }
        if competencia:
            pass
        else:
            for r in self.get_respuestas():
                if r.respuesta > 0: total += r.respuesta
            if total > 0:
                _sum_ = Conducta.objects.values('id').annotate(v=Max('conductavalor__valor')).aggregate(Sum('v'))
                porciento = total / _sum_['v__sum']
                inverso = 1 - ( total/_sum_['v__sum'] )
            calificacion = {
                'total': total,
                'porciento': int(porciento * 100),
                'inverso': int(inverso*100)
            }
            # Usando puntos
            if total <= 75:
                calificacion['nivel'] = 'Recomendado'
                calificacion['primary_color'] = COLORS['primary'][0]
                calificacion['secondary_color'] = COLORS['secondary'][0]
                # Valores estáticos
                calificacion['inverso'] = int(100 - total/(75)*33)
            elif total >= 76 and total <= 83:
                calificacion['nivel'] = 'Con Reserva'
                calificacion['primary_color'] = COLORS['primary'][2]
                calificacion['secondary_color'] = COLORS['secondary'][2]
                # Valores estáticos
                calificacion['inverso'] = int(100 - (33+((total-76)/(83-76))*33))
            else:
                calificacion['nivel'] = 'No Recomendado'
                calificacion['primary_color'] = COLORS['primary'][3]
                calificacion['secondary_color'] = COLORS['secondary'][3]
                # Valores estáticos
                calificacion['inverso'] = int(100 - (67+((total-84)/(_sum_['v__sum']-84))*33))
            # Usando Porcentajes
            #if inverso <= 0.33:
            #    calificacion['nivel'] = 'No Recomendado'
            #    calificacion['primary_color'] = COLORS['primary'][3]
            #    calificacion['secondary_color'] = COLORS['secondary'][3]
            #elif inverso <= 0.66:
            #    calificacion['nivel'] = 'Con Reserva'
            #    calificacion['primary_color'] = COLORS['primary'][2]
            #    calificacion['secondary_color'] = COLORS['secondary'][2]
            #else:
            #    calificacion['nivel'] = 'Recomendado'
            #    calificacion['primary_color'] = COLORS['primary'][0]
            #    calificacion['secondary_color'] = COLORS['secondary'][0]            
        return calificacion
    
    def get_respuestas(self):
        return EvaluacionRespuesta.objects.filter(evaluacion=self).order_by('conducta__orden')

    def get_resultados(self):
        """
            Resultados generales por competencia
        """
        respuestas = self.get_respuestas()
        resultados = []
        #print("== Evaluacion {} ==".format(self.nombre_persona))
        for competencia in Competencia.objects.all().order_by('nombre'):
            try:                
                nivel = 'Sin calificación'
                nivel_n = 3                
                clase = ''
                total = 0
                inverso = -1
                for r in respuestas.filter(conducta__competencia=competencia):
                    #print(competencia, r.conducta, r.respuesta)
                    if r.respuesta > 0: total += r.respuesta                
                if total >= 0 and respuestas.filter(conducta__competencia=competencia, respuesta__gte=0).count() > 0:
                    porciento = total/competencia.get_sum_total()
                    inverso = 1-(total/competencia.no_apto_max)
                    # Apto
                    if total >= competencia.apto_min and total <= competencia.apto_max:
                        nivel = 'Recomendado'
                        nivel_n = 0
                        if competencia.apto_max == competencia.apto_min:
                            factor = 1
                        else:
                            factor = competencia.apto_max-competencia.apto_min
                        inverso = 100 - ((total-competencia.apto_min)/factor)*33
                    # Apto Condicionado
                    elif total >= competencia.apto_condicionado_min and total <= competencia.apto_condicionado_max:
                        nivel = 'Con Reserva'
                        nivel_n = 2
                        if competencia.apto_condicionado_max == competencia.apto_condicionado_min:
                            factor = 1
                        else:
                            factor = competencia.apto_condicionado_max-competencia.apto_condicionado_min
                        inverso = 100 - (33+((total-competencia.apto_condicionado_min)/factor)*33)
                    # No Apto
                    elif total >= competencia.no_apto_min and total <= competencia.no_apto_max:
                        nivel = 'No Recomendado'
                        nivel_n = 3
                        if competencia.no_apto_max == competencia.no_apto_min:
                            factor = 1
                        else:
                            factor = competencia.no_apto_max-competencia.no_apto_min
                        inverso = 100 - (66+((total-competencia.no_apto_min)/factor)*33)
                    # Porcentajes
                    #if inverso <= 0.33:
                    #    nivel = 'No Recomendado'
                    #    nivel_n = 3
                    #elif inverso <= 0.66:
                    #    nivel = 'Con Reserva'
                    #    nivel_n = 2
                    #else:
                    #    nivel = 'Recomendado'
                    #    nivel_n = 0
                
                resultados.append({
                    'competencia': competencia,
                    'total': total,
                    'nivel': nivel,
                    'nivel_n': nivel_n,
                    'inverso': int(inverso),
                    'primary_color': COLORS['primary'][nivel_n],
                    'secondary_color': COLORS['secondary'][nivel_n],
                    #'porciento': int(porciento * 100),
                    #'class': clase,
                    #'totales': competencia.get_barras(total)
                })
            except Exception as e:
                print('Error: {}'.format(e))
                resultados[competencia.nombre] = 0
        return resultados

class EvaluacionRespuesta(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    conducta = models.ForeignKey(Conducta, on_delete=models.CASCADE)
    respuesta = models.IntegerField(default=-1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.respuesta) 

    def get_conducta_valores(self):
        return ConductaValor.objects.filter(conducta=self.conducta)
