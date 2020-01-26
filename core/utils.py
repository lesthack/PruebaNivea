from .models import *

def inserts():
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
