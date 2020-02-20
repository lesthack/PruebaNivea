# -*- coding: utf-8 -*-
from django.forms import *
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import *

class evaluacionForm(ModelForm):
    class Meta:
        model = Evaluacion
        fields = [
            'nombre_persona',
            'fecha',
            'edad',
            'sexo',
            'estado_civil',
            'escolaridad',
            'localidad',
            'numero_hijos'
        ]
        widgets = {
            'fecha': TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha', 'type': 'date'}),
        }

    def __init__(self, user, *args, **kwargs):
        super(evaluacionForm, self).__init__(*args, **kwargs)
        self.fields['nombre_persona'].widget.attrs = {
            'class': 'form-control',
            'type': 'number',
            'placeholder': 'Nombre Persona'
        }
        self.fields['edad'].widget.attrs = {
            'class': 'form-control',
            'type': 'number',
            'placeholder': 'Edad'
        }
        #print(self.fields['sexo'].choices)
        #self.fields['sexo'].widget = RadioSelect(choices=self.fields['sexo'].choices)
        self.fields['sexo'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado_civil'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['escolaridad'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['localidad'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['numero_hijos'].widget.attrs = {
            'class': 'form-control'
        }
        self.user = user

