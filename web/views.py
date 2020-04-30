from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views import View
from django.core.exceptions import PermissionDenied
from django.db import connection, transaction
from django.utils.html import escape
from core.models import *
from core.forms import *

class EvaluacionesList(ListView):
  model = Evaluacion
  template_name = 'evaluacion_list.html'
  paginate_by = 10
  ordering = ['-created_at']

  def get_queryset(self):
    query = self.request.GET.get('q')
    object_list = self.model.objects.all()
    if query:
        object_list = object_list.filter(nombre_persona__icontains=query)
    return object_list

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['competencias'] = Competencia.objects.all().order_by('nombre')
    context['sugerencia_nombres'] = Evaluacion.objects.all().values('nombre_persona')
    context['q'] = self.request.GET.get('q','')
    return context


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

  return render(request, 'login.html', {
        'message': message
    }
)

@login_required(login_url='/auth')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/auth')
def index(request):
    return HttpResponseRedirect('/evaluaciones/')

@login_required(login_url='/auth')
def evaluaciones(request):
    list_evaluaciones = Evaluacion.objects.all().order_by('-created_at')
    list_competencias = Competencia.objects.all().order_by('nombre')
    return render(request, 'evaluaciones.html', {
        'evaluaciones': list_evaluaciones,
        'competencias': list_competencias
    })

@login_required(login_url='/auth')
def evaluacion_view(request, evaluacion_id):
    try:
        view_evaluacion = Evaluacion.objects.get(id=evaluacion_id)
    except Evaluacion.DoesNotExist:
        #agregar redirect a pagina que diga que no existe la eval
        return HttpResponseRedirect('/evaluaciones/')
    return render(request, 'evaluacion.html',{
        'evaluacion': view_evaluacion,
    })

@login_required(login_url='/auth')
def evaluacion_new(request):
    if request.method == 'POST':
        form_evaluacion = evaluacionForm(request.user, request.POST)
        if form_evaluacion.is_valid():
            new_evaluacion = form_evaluacion.save(commit=False)
            new_evaluacion.created_by = request.user
            new_evaluacion.save()
            return HttpResponseRedirect('/evaluaciones/e/{}/q/'.format(new_evaluacion.id))
    else:
        form_evaluacion = evaluacionForm(request.user)
    return render(request, 'evaluacion_form.html', {
        'form': form_evaluacion
    })

@login_required(login_url='/auth')
def evaluacion_edit(request, evaluacion_id):
    try:
        view_evaluacion = Evaluacion.objects.get(id=evaluacion_id)
        if request.method == 'POST':
            form_evaluacion = evaluacionForm(request.user, request.POST, instance=view_evaluacion)
            if form_evaluacion.is_valid():
                view_evaluacion = form_evaluacion.save()
                return HttpResponseRedirect('/evaluaciones/v/{}/'.format(view_evaluacion.id))
        else:
            form_evaluacion = evaluacionForm(request.user, instance=view_evaluacion)
    except Evaluacion.DoesNotExist:
        #agregar redirect a pagina que diga que no existe la eval
        return HttpResponseRedirect('/evaluaciones/')
    return render(request, 'evaluacion_form.html', {
        'form': form_evaluacion
    })

@login_required(login_url='/auth')
def evaluacion_quiz(request, evaluacion_id):
    try:
        view_evaluacion = Evaluacion.objects.get(id=evaluacion_id)
        if request.method == 'POST':
            for r in request.POST:
                if 'respuesta_' in r:
                    respuesta_id = int(r[10:])
                    view_respuesta = EvaluacionRespuesta.objects.get(id=respuesta_id)
                    view_respuesta.respuesta = int(request.POST[r])
                    view_respuesta.save()
            return HttpResponseRedirect('/evaluaciones/v/{}/'.format(view_evaluacion.id))
        list_respuestas_1 = view_evaluacion.get_respuestas().filter(
            conducta__orden__gte=1, 
            conducta__orden__lte=38
        )
        list_respuestas_2 = view_evaluacion.get_respuestas().filter(
            conducta__orden__gte=39,
            conducta__orden__lte=61
        )
        list_respuestas_3 = view_evaluacion.get_respuestas().filter(
            conducta__orden__gte=62,
            conducta__orden__lte=80
        )
    except Evaluacion.DoesNotExist:
        print('No sen encontró la evaluacion')
        return HttpResponseRedirect('/evaluaciones/')
    return render(request, 'evaluacion_quiz.html', {
        'evaluacion': view_evaluacion,
        'respuestas1': list_respuestas_1,
        'respuestas2': list_respuestas_2,
        'respuestas3': list_respuestas_3,
    })

@login_required(login_url='/auth')
def evaluacion_remove(request, evaluacion_id):
    try:
        view_evaluacion = Evaluacion.objects.get(id=evaluacion_id)
        view_evaluacion.delete()
    except Evaluacion.DoesNotExist:
        #agregar redirect a pagina que diga que no existe la eval
        return HttpResponseRedirect('/evaluaciones/')
    return HttpResponseRedirect('/evaluaciones/')

@login_required(login_url='/auth')
def profile_form(request):
    if request.method == 'POST':
        if 'username' in request.POST:
            form = profileForm(request.POST, instance=request.user)
            if form.is_valid():
                view_user = form.save(commit=False)
                view_user.save()
        else:
            form = profileForm(instance=request.user)
        if 'old_password' in request.POST:
            form_password = MyPasswordChangeForm(request.user, request.POST)
            if form_password.is_valid():
                print("ok")
                pass
        else:
            form_password = MyPasswordChangeForm(request.user)
    else:
        form = profileForm(instance=request.user)
        form_password = MyPasswordChangeForm(request.user)
    return render(request, 'profile_form.html', {
        'form': form,
        'form_password': form_password,
    })

@login_required(login_url='/auth')
def json_nombres(request):
    #if not request.is_ajax():
    #    return HttpResponseRedirect('/evaluaciones/')
    query = request.GET.get('q')
    list_nombres = Evaluacion.objects.all().order_by('nombre_persona')
    if query:
        list_nombres = list_nombres.filter(nombre_persona__icontains=query)
    else:
        list_nombres = list_nombres[0:10]
    json_list = [item.nombre_persona for item in list_nombres]
    return JsonResponse(json_list, safe=False)
