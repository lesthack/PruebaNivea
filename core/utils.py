# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from .models import *
from datetime import datetime
from .datos import *

def inserts_localidades():
    Localidad.objects.get_or_create(nombre='Guanajuato')
    Localidad.objects.get_or_create(nombre='Irapuato')
    Localidad.objects.get_or_create(nombre='León')
    Localidad.objects.get_or_create(nombre='Romita')
    Localidad.objects.get_or_create(nombre='Silao')

def inserts_escalas():
    # Escalas
    escala_fv, c = Escala.objects.get_or_create(nombre='Falso-Verdadero')
    if escala_fv:
        falso = EscalaItem.objects.get_or_create(escala=escala_fv, nombre='Falso')
        verdadero = EscalaItem.objects.get_or_create(escala=escala_fv, nombre='Verdadero')
    # Likert 1
    escala_likert1, c = Escala.objects.get_or_create(nombre='Likert1')
    if escala_likert1:
        nunca = EscalaItem.objects.get_or_create(escala=escala_likert1, nombre='Nunca')
        algunas_veces = EscalaItem.objects.get_or_create(escala=escala_likert1, nombre='Algunas Veces')
        frecuentemente = EscalaItem.objects.get_or_create(escala=escala_likert1, nombre='Frecuentemente')
        muy_frecuentemente = EscalaItem.objects.get_or_create(escala=escala_likert1, nombre='Muy Frecuentemente')
    # Likert 2
    escala_likert2, c = Escala.objects.get_or_create(nombre='Likert2')
    if escala_likert2:
        nada = EscalaItem.objects.get_or_create(escala=escala_likert2, nombre='Nada')
        poco = EscalaItem.objects.get_or_create(escala=escala_likert2, nombre='Poco')
        moderadamente = EscalaItem.objects.get_or_create(escala=escala_likert2, nombre='Moderadamente')
        bastante = EscalaItem.objects.get_or_create(escala=escala_likert2, nombre='Bastante')
        muchisimo = EscalaItem.objects.get_or_create(escala=escala_likert2, nombre='Muchisimo')

def inserts_competencias():
    for compe in lista_competencias.keys():
        Competencia.objects.get_or_create(
            nombre = compe,
            descripcion = lista_competencias[compe]['descripcion'],
            apto = lista_competencias[compe]['apto'],
            apto_min = lista_competencias[compe]['apto_min'],
            apto_max = lista_competencias[compe]['apto_max'],
            apto_condicionado = lista_competencias[compe]['apto_condicionado'],
            apto_condicionado_min = lista_competencias[compe]['apto_condicionado_min'],
            apto_condicionado_max = lista_competencias[compe]['apto_condicionado_max'],
            no_apto = lista_competencias[compe]['no_apto'],
            no_apto_min = lista_competencias[compe]['no_apto_min'],
            no_apto_max = lista_competencias[compe]['no_apto_max'],
        )

def inserts_conductas():
    for nombre_escala in lista_conductas.keys():
        view_escala = Escala.objects.get(nombre=nombre_escala)
        lista_escala = list(view_escala.getItems())
        for pregunta in lista_conductas[nombre_escala]:
            new_conducta, c = Conducta.objects.get_or_create(
                pregunta = pregunta[1],
                orden = pregunta[0],
                escala = view_escala,
                invertido = pregunta[2]
            )
            if new_conducta:
                for i in range(len(pregunta[3])):
                    ConductaValor.objects.get_or_create(
                        conducta = new_conducta,
                        escala_item = lista_escala[i],
                        valor = pregunta[3][i]
                    )

def inserts_competencias_conductas():
    for nombre_competencia in lista_competencias_conductas.keys():
        view_competencia = Competencia.objects.get(nombre=nombre_competencia)
        for i in lista_competencias_conductas[nombre_competencia]:
            view_conducta = Conducta.objects.get(orden=i)
            view_conducta.competencia.add(view_competencia)

def inserts_all():
    inserts_localidades()
    inserts_escalas()
    inserts_competencias()
    inserts_conductas()
    inserts_competencias_conductas()

def patch1():
    """
      Patch para cambios del 21 de Marzo, 2020
    """
    # Localidades
    try:
        Localidad.objects.get_or_create(id=-1, nombre='No Definido')
        print('Localidad "No Definida" agregada.')
    except Exception as e:
        print('Error: ', e)
    # Competencias
    for nombre_competencia in lista_competencias.keys():
        view_competencia = Competencia.objects.get(nombre=nombre_competencia)
        view_competencia.no_apto_max = lista_competencias[nombre_competencia]['no_apto_max']
        view_competencia.save()
        print('{} actualizada'.format(nombre_competencia))

def patch2():
    """
        Patch para cambios del 18 de Agosto, 2020
    """
    print('Patch2 :: 18 Agosto 2020')
    # Competencias
    for nombre_competencia in lista_competencias.keys():
        view_competencia = Competencia.objects.get(nombre=nombre_competencia)
        view_competencia.tipo = lista_competencias[nombre_competencia]['tipo']
        view_competencia.contra_titulo = lista_competencias[nombre_competencia]['contra_titulo']
        view_competencia.save()
        print('{} actualizada'.format(nombre_competencia))
