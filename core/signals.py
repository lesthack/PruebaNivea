# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from .models import *

@receiver(post_save, sender=Evaluacion)
def nueva_evaluacion(sender, instance, **kwargs):
    """
      Descripcion:
        Cuando se crea una nueva evaluación,
        se autogeneran las respuestas
    """
    for conducta_view in Conducta.objects.all():
        EvaluacionRespuesta.objects.get_or_create(
            evaluacion = instance,
            conducta = conducta_view,
            created_by = instance.created_by
        )
