from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib.admin import site
from django.conf import settings
from django.contrib import admin
from django.urls import path

admin.site.site_header = "Proyecto Nivea"
admin.site.site_title = "Nivea"

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/admin')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
