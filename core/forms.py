# -*- coding: utf-8 -*-
from django.forms import *
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from core.models import *

class evaluacionForm(ModelForm):
    class Meta:
        model = Evaluacion
        fields = [
            'nombre_persona',
            'fecha',
            'fecha_nacimiento',
            #'edad',
            #'sexo',
            #'estado_civil',
            #'escolaridad',
            #'localidad',
            #'numero_hijos'
        ]
        widgets = {
            'fecha': TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha', 'type': 'date'}),
            'fecha_nacimiento': TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha', 'type': 'date'}),
        }

    def __init__(self, user, *args, **kwargs):
        super(evaluacionForm, self).__init__(*args, **kwargs)
        self.fields['nombre_persona'].widget.attrs = {
            'class': 'form-control',
            'type': 'number',
            'placeholder': 'Nombre Persona'
        }
        #self.fields['edad'].widget.attrs = {
        #    'class': 'form-control',
        #    'type': 'number',
        #    'placeholder': 'Edad'
        #}
        #self.fields['sexo'].widget.attrs = {
        #    'class': 'form-control'
        #}
        #self.fields['estado_civil'].widget.attrs = {
        #    'class': 'form-control'
        #}
        #self.fields['escolaridad'].widget.attrs = {
        #    'class': 'form-control'
        #}
        #self.fields['localidad'].widget.attrs = {
        #    'class': 'form-control'
        #}
        #self.fields['numero_hijos'].widget.attrs = {
        #    'class': 'form-control'
        #}
        self.user = user

class profileForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]

    def __init__(self, *args, **kwargs):
        super(profileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'Nombre de Usuario',
            'readonly': True
        }
        self.fields['first_name'].widget.attrs = {
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'Nombres',
        }
        self.fields['last_name'].widget.attrs = {
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'Apellidos',
        }
        self.fields['email'].widget.attrs = {
            'class': 'form-control',
            'type': 'email',
            'placeholder': 'Email',
        }

class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['new_password1'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['new_password2'].widget.attrs = {
            'class': 'form-control'
        }
