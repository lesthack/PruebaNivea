from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib.admin import site
from django.conf import settings
from django.contrib import admin
from django.urls import path
from web.views import *

admin.site.site_header = "Proyecto Nivea"
admin.site.site_title = "Nivea"

urlpatterns = [
    url(r'^$', index),
    url(r'^auth/$', auth),
    url(r'^logout/$', logout_user),
    url(r'^evaluaciones/$', EvaluacionesList.as_view()),
    url(r'^evaluaciones/v/(?P<evaluacion_id>\d+)/$', evaluacion_view),
    url(r'^evaluaciones/e/(?P<evaluacion_id>\d+)/$', evaluacion_edit),
    url(r'^evaluaciones/e/(?P<evaluacion_id>\d+)/q/$', evaluacion_quiz),
    url(r'^evaluaciones/d/(?P<evaluacion_id>\d+)/$', evaluacion_remove),
    url(r'^evaluaciones/n/$', evaluacion_new),
    url(r'^test/$', site.admin_view(test)),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
