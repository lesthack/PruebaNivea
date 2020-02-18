from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import PermissionDenied
from django.db import connection, transaction
from django.utils.html import escape

def index(request):
    return render(request, 'base_site.html', 
        {}
    )

def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")
