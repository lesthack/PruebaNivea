# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from .models import *

@receiver(post_save, sender=Aplicacion)
def nueva_aplicacion(sender, instance, **kwargs):
    """
      Descripcion:
        Cuando se crea una nueva aplicacion, se deben crear
        los Items según el instrumento elegido
    """
    #for instrumento_item in InstrumentoItem.objects.filter(instrumento=instance.instrumento):
    #    aplicacion_item = AplicacionItem(
    #        aplicacion = instance,
    #        item = instrumento_item,
    #        created_by = instance.created_by
    #    ).save()
