# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from core.models import *
from django.utils.safestring import mark_safe
import datetime

admin.site.register(Categoria)
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

class instrumentoForm(forms.ModelForm):
    class Meta:
        model = Instrumento
        exclude = ['created_by']

@admin.register(Instrumento)
class instrumentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'created_by', 'created_at']
    form = instrumentoForm

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()

@admin.register(InstrumentoValor)
class instrumentoValorAdmin(admin.ModelAdmin):
    list_display = ['pregunta', 'nombre_escala', 'nombre_item', 'valor']
    list_filter = ['instrumento_item__pregunta']
    ordering = ['instrumento_item__orden', 'id']

class instrumentoItemForm(forms.ModelForm):
    class Meta:
        model = InstrumentoItem
        exclude = ['created_by']

@admin.register(InstrumentoItem)
class instrumentoItemAdmin(admin.ModelAdmin):
    list_display = ['orden', 'pregunta']
    list_filter = ['instrumento']
    ordering = ['orden']
    form = instrumentoItemForm

class aplicacionForm(forms.ModelForm):
    class Meta:
        model = Aplicacion
        exclude = ['created_by']

@admin.register(Aplicacion)
class aplicacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'created_by']
    form = aplicacionForm
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()
 
#class aplicacionItemForm(forms.ModelForm):
#    class Meta:
#        model = AplicacionItem
#        exclude = ['created_by']
#        widgets = {
#            'respuesta': forms.RadioSelect
#        }
#
#    def __init__(self, *args, **kwargs):
#        super(aplicacionItemForm, self).__init__(*args, **kwargs)
#        if self.instance:
#            view_escala = [(i.id, i.nombre) for i in EscalaItem.objects.filter(escala=self.instance.item.escala)]
#            self.fields['respuesta'] = forms.ChoiceField(choices=view_escala, widget=forms.RadioSelect)
#
#aplicationItemInlineFormSet = forms.inlineformset_factory(Aplicacion, AplicacionItem, fields=['item', 'respuesta'], can_delete=False)

#@admin.register(AplicacionItem)
#class aplicacionItemAdmin(admin.ModelAdmin):
#    list_display = ['item', 'respuesta', 'created_at', 'created_by']
#    form = aplicacionItemForm
#
#    def save_model(self, request, obj, form, change):
#        if not change:
#            obj.created_by = request.user
#        obj.save()
