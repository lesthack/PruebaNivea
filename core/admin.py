# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from core.models import *
import datetime

admin.site.register(Escala)
admin.site.register(EscalaItem)

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

class instrumentoItemForm(forms.ModelForm):
    class Meta:
        model = InstrumentoItem
        exclude = ['created_by']

@admin.register(InstrumentoItem)
class instrumentoItemAdmin(admin.ModelAdmin):
    list_display = ['instrumento','pregunta', 'escala', 'grupo']
    form = instrumentoItemForm

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()

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

class aplicacionItemForm(forms.ModelForm):
    class Meta:
        model = AplicacionItem
        exclude = ['created_at', 'updated_at', 'created_by']

    def __init__(self, *args, **kwargs):
        super(aplicacionItemForm, self).__init__(*args, **kwargs)
        obj = self.fields['item'].queryset.model
        print(obj.escala)
        self.fields['respuesta'].queryset = EscalaItem.objects.filter(escala_id=1)
        #self.fields['category'].queryset = Category.objects.filter(user=user)

@admin.register(AplicacionItem)
class aplicacionItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'respuesta', 'created_at', 'created_by']
    form = aplicacionItemForm

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()
