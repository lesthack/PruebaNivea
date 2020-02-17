# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from core.models import *
from django.utils.safestring import mark_safe
import datetime

admin.site.register(Competencia)
admin.site.register(Localidad)

@admin.register(Escala)
class escalaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'go_items']
    ordering = ['id']

@admin.register(EscalaItem)
class escalaItemAdmin(admin.ModelAdmin):
    list_display = ['nombre_escala', 'nombre']
    list_filter = ['escala__nombre']
    ordering = ['escala__nombre', 'id']

@admin.register(Conducta)
class conductaAdmin(admin.ModelAdmin):
    list_display = ['orden', 'pregunta', 'escala', 'invertido']
    list_filter = ['escala__nombre']
    ordering = ['orden']

@admin.register(ConductaValor)
class conductaValorAdmin(admin.ModelAdmin):
    list_display = ['conducta', 'escala_item', 'valor']
    list_filter = ['conducta']
    ordering = ['conducta__orden']

class evaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        exclude = ['created_by']

@admin.register(Evaluacion)
class evaluacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'created_by']
    form = evaluacionForm
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()
 
class evaluacionRespuestaForm(forms.ModelForm):
    class Meta:
        model = EvaluacionRespuesta
        exclude = ['created_by']
        widgets = {
            'respuesta': forms.RadioSelect
        }

    def __init__(self, *args, **kwargs):
        super(evaluacionRespuestaForm, self).__init__(*args, **kwargs)
        if self.instance:
            view_escala = [(i.id, i.nombre) for i in EscalaItem.objects.filter(escala=self.instance.conducta.escala)]
            self.fields['respuesta'] = forms.ChoiceField(choices=view_escala, widget=forms.RadioSelect)

#aplicationItemInlineFormSet = forms.inlineformset_factory(Aplicacion, AplicacionItem, fields=['item', 'respuesta'], can_delete=False)

@admin.register(EvaluacionRespuesta)
class evaluacionRespuestaAdmin(admin.ModelAdmin):
    list_display = ['evaluacion', 'conducta', 'respuesta', 'created_at', 'created_by']
    list_filter = ['evaluacion']
    ordering = ['conducta__orden']
    form = evaluacionRespuestaForm

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()
