# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from .models import *
from datetime import datetime

def inserts_escalas():
    # Escalas
    escala_fv, c = Escala.objects.get_or_create(nombre='Falso-Verdadero')
    if escala_fv:
        falso = EscalaItem.objects.get_or_create(escala=escala_fv, nombre='Falso', valor=0)
        verdadero = EscalaItem.objects.get_or_create(escala=escala_fv, nombre='Verdadero', valor=1)
    escala_likert, c = Escala.objects.get_or_create(nombre='Likert')
    if escala_likert:
        nunca = EscalaItem.objects.get_or_create(escala=escala_likert, nombre='Nunca', valor=0)
        algunas_veces = EscalaItem.objects.get_or_create(escala=escala_likert, nombre='Algunas Veces', valor=1)
        frecuentemente = EscalaItem.objects.get_or_create(escala=escala_likert, nombre='Frecuentemente', valor=2)
        muy_frecuentemente = EscalaItem.objects.get_or_create(escala=escala_likert, nombre='Muy frecuentemente', valor=3)

def inserts_instrumento():
    me = User.objects.get(id=1)
    instrumento_ejemplo, c = Instrumento.objects.get_or_create(nombre='Ejemplo', created_by=me)
    escala_falsoverdadero = Escala.objects.get(nombre='Falso-Verdadero')
    escala_likert = Escala.objects.get(nombre='Likert')

    items = [
        u'¿Alguno de tus amigos ha usado drogas?',
        u'¿Alguno de tus amigos ha tenido problemas con las autoridades?',
        u'¿Se han aburrido tus amigos en las fiestas donde no hay tragos?',
        u'¿Alguno de tus amigos le ha vendido o regalado drogas a un compañero?',
        u'¿Tus amigos han robado algo en un almacén o causado daño a propósito?',
        u'¿Has molestado o le has hecho daño a los animales?',
        u'¿Has amenazado a otros con hacerles daño o lastimarlos?',
        u'¿Has dañado intencionalmente las cosas de otros?',
        u'¿Has tenido más peleas que la mayoría de tus compañeros?',
        u'Me gusta cambiar con frecuencia de trabajo.',
        u'He estado en la cárcel.',
        u'Me interesa dedicar tiempo a cosas que las que no puedo obtener un beneficio inmediato.',
        u'Me han arrestado en alguna ocasión.',
        u'Nunca me he peleado físicamente con mis amigos o familiares.',
        u'No me importa mentir a alguien si con ello me evito problemas.',
        u'Nunca he probado drogas ilegales.',
        u'Me han despedido más de una vez del trabajo.',
        u'A veces me he saltado las normas para conseguir algo que de todas maneras me correspondía.',
        u'Me gusta viajar de un sitio a otro, sin tener que quedarme en ninguna parte.',
        u'Las decisiones que afectan a mi vida y a mi trabajo las tomo con mucha rapidez.',
        u'Evito hacer cosas excitantes o divertidas, si son peligrosas.',
        u'Me gusta o gustaría manejar de prisa.',
        u'Suelo faltar al trabajo',
        u'Durante mi adolescencia me escapé alguna vez de casa y pasé la noche fuera.',
        u'Guiarse por la astucia es mejor que guiarse por las reglas.',
        u'Mentir es malo solo si te descubren.',
        u'Me opongo sistemáticamente a las normas porque restringen la libertad de la gente.',
    ]
    for i in items:
        item1, c1 = InstrumentoItem.objects.get_or_create(
            instrumento = instrumento_ejemplo,
            pregunta = i,
            descripcion = '',
            escala = escala_falsoverdadero,
            grupo = 'Parte 1',
            created_by = me
        )

def inserts_aplicacion_ejemplo():
    me = User.objects.get(id=1)
    instrumento_ejemplo = Instrumento.objects.get(nombre='Ejemplo', created_by=me)
    aplicacion_ejemplo, c = Aplicacion.objects.get_or_create(
        fecha = datetime.now(),
        edad = 18,
        sexo = 0,
        escolaridad = 2,
        estado_civil = 1,
        puesto = 'Ejemplo',
        instrumento = instrumento_ejemplo,
        created_by = me
    )
