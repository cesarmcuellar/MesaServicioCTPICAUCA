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
    path('listarCasosAsignados/', views.listarCasosAsignadosTecnico),
    path('solucionarCaso/', views.solucionarCaso),
    path('vistaGestionarUsuarios/', views.vistaGestionarUsuarios),
    path('vistaRegistrarUsuario/', views.vistaRegistrarUsuario),
    path('registrarUsuario/', views.registrarUsuario),
    path('recuperarClave/', views.recuperarClave),
    path('reportesEstadisticos/', views.estadisticas),

    path('pdfSolicitudes/', views.generarPdfSolicitudes),

    path('salir/', views.salir),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
