from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

tipoOficinaAmbiente = [
    ('Administrativo', 'Administrativo'),
    ('Formación', 'Formación')
]

tipoUsuario = [
    ('Administrativo', 'Administrativo'),
    ('Instructor', 'Instructor')
]

estadoCaso = [
    ('Solicitada', 'Solicitada'),
    ('En Proceso', 'En Proceso'),
    ('Finalizada', 'Finalizada')
]

tipoSolucion = [
    ('Parcial', 'Parcial'),
    ('Definitiva', 'Definitiva')
]


class OficinaAmbiente(models.Model):
    ofiTipo = models.CharField(max_length=15, choices=tipoOficinaAmbiente,
                               db_comment="tipo de oficina")
    ofiNombre = models.CharField(max_length=50, unique=True,
                                 db_comment="Nombre de la oficina o ambiente")
    fechaHoraCreacion = models.DateTimeField(auto_now_add=True,
                                             db_comment="Fecha y hora del registro")
    fechaHoraActualizacion = models.DateTimeField(auto_now=True,
                                                  db_comment="Fecha y hora última actualización")

    def __str__(self) -> str:
        return self.ofiNombre


class User(AbstractUser):
    userTipo = models.CharField(
        max_length=15, choices=tipoUsuario, db_comment="Tipo de usuario")
    userFoto = models.ImageField(
        upload_to=f"fotos/", null=True, blank=True, db_comment="Foto del Usuario")
    fechaHoraCreacion = models.DateTimeField(auto_now_add=True,
                                             db_comment="Fecha y hora del registro")
    fechaHoraActualizacion = models.DateTimeField(auto_now=True,
                                                  db_comment="Fecha y hora última actualización")

    def __str__(self) -> str:
        return self.username


class Solicitud(models.Model):
    solUsuario = models.ForeignKey(User, on_delete=models.PROTECT,
                                   db_comment="Hace referencia al empleado que hace la solicitud")
    solDescripcion = models.TextField(max_length=1000,
                                      db_comment="Texto que describe las solicitud del empleado")
    solOficinaAmbiente = models.ForeignKey(
        OficinaAmbiente, on_delete=models.PROTECT,
        db_comment="Hace referencia a la oficina o ambiente donde se encuentra el equipo de la solicitud")
    fechaHoraCreacion = models.DateTimeField(auto_now_add=True,
                                             db_comment="Fecha y hora del registro")
    fechaHoraActualizacion = models.DateTimeField(auto_now=True,
                                                  db_comment="Fecha y hora última actualización")

    def __str__(self) -> str:
        return self.solDescripcion


class Caso(models.Model):
    casSolicitud = models.ForeignKey(Solicitud, on_delete=models.PROTECT,
                                     db_comment="Hace referencia a la solicitud que generó el Caso")
    casCodigo = models.CharField(max_length=20, unique=True,
                                 db_comment="Código único del caso")
    casUsuario = models.ForeignKey(User, on_delete=models.PROTECT,
                                   db_comment="Empleado de soporte técnico asignado al caso")
    casEstado = models.CharField(
        max_length=15, choices=estadoCaso, default='Solicitada')

    # fechaHoraCreacion = models.DateTimeField(auto_now_add=True,
    #                                        db_comment="Fecha y hora del registro")
    fechaHoraActualizacion = models.DateTimeField(auto_now=True,
                                                  db_comment="Fecha y hora última actualización")

    def __str__(self) -> str:
        return f"{self.casCodigo}"


class TipoProcedimiento(models.Model):
    tipNombre = models.CharField(
        max_length=20, unique=True, db_comment="nombre del tipo de procedimiento")
    tipDescripcion = models.TextField(max_length=1000, null=True,
                                      db_comment="Aquí se hace una descripción del tipo de procedimiento")

    fechaHoraCreacion = models.DateTimeField(auto_now_add=True,
                                             db_comment="Fecha y hora del registro")
    fechaHoraActualizacion = models.DateTimeField(auto_now=True,
                                                  db_comment="Fecha y hora última actualización")

    def __str__(self) -> str:
        return self.tipNombre


class SolucionCaso(models.Model):
    solCaso = models.ForeignKey(Caso, on_delete=models.PROTECT,
                                db_comment="Hace referencia al caso que genera la solución")
    solProcedimiento = models.TextField(max_length=2000,
                                        db_comment="Texto del procedimiento realizado en la solución del caso")
    solTipoSolucion = models.CharField(max_length=20, choices=tipoSolucion,
                                       db_comment="Tipo de la solucuín, si es parcial o definitiva")
    fechaHoraCreacion = models.DateTimeField(auto_now_add=True,
                                             db_comment="Fecha y hora del registro")
    fechaHoraActualizacion = models.DateTimeField(auto_now=True,
                                                  db_comment="Fecha y hora última actualización")

    def __str__(self) -> str:
        return self.solTipoSolucion


class SolucionCasoTipoProcedimientos(models.Model):
    solSolucionCaso = models.ForeignKey(SolucionCaso, on_delete=models.PROTECT,
                                        db_comment="Hace referencia a la solución del Caso")
    solTipoProcedimiento = models.ForeignKey(TipoProcedimiento, on_delete=models.PROTECT,
                                             db_comment="Hace referencia al tipo de procedimiento de la solución")
