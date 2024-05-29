from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.inicio),
    path('login/', views.login),
    path('inicioAdministrador/', views.inicioAdministrador),
    path('inicioTecnico/', views.inicioTecnico),
    path('inicioEmpleado/', views.inicioEmpleado),
    path('vistaSolicitud/', views.vistaSolicitud),
    path('registrarSolicitud/', views.registrarSolicitud),
    path('listarCasosParaAsignar/', views.listarCasos),
    path('asignarTecnicoCaso/', views.asignarTecnicoCaso),
    path('salir/', views.salir),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
