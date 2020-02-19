from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import PermissionDenied
from django.db import connection, transaction
from django.utils.html import escape
from core.models import *

@csrf_protect
def auth(request, incognito=False):
  if request.user.is_authenticated:
    return HttpResponseRedirect(request.GET.get('next','/'))

  username = ''
  password = ''
  message = ''

  if request.POST:
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
      if user.is_active:
        login(request, user)
        return HttpResponseRedirect(request.GET.get('next','/'))
      else:
        message = u'El usuario no se encuentra activo.'
    else:
      message = u'Usuario y/o contraseña incorrectos'
  print(message)
  return render(request, 'login.html', {
        'message': message
    }
)

@login_required(login_url='/auth')
def index(request):
    return render(request, 'base_site.html', {})

@login_required(login_url='/auth')
def evaluaciones(request):
    list_evaluaciones = Evaluacion.objects.all().order_by('-created_at')
    return render(request, 'evaluaciones.html', {
        'evaluaciones': list_evaluaciones
    })

@login_required(login_url='/auth')
def evaluacion(request, evaluacion_id):
    return render(request, 'evaluacion.html',{})

@login_required(login_url='/auth')
def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")
