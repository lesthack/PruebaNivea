# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from core.models import *
import datetime

admin.site.register(Escala)
admin.site.register(ItemEscala)
admin.site.register(Instrumento)
admin.site.register(ItemInstrumento)
admin.site.register(Aplicacion)

class aplicacionItemForm(forms.ModelForm):
    class Meta:
        model = AplicacionItem
        exclude = ['created_at', 'updated_at', 'created_by']

    def __init__(self, *args, **kwargs):
        super(aplicacionItemForm, self).__init__(*args, **kwargs)
        obj = self.fields['item'].queryset.model
        print(obj.escala)
        self.fields['respuesta'].queryset = ItemEscala.objects.filter(escala_id=1)
        #self.fields['category'].queryset = Category.objects.filter(user=user)

@admin.register(AplicacionItem)
class aplicacionItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'respuesta', 'created_at', 'created_by']
    form = aplicacionItemForm

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()
