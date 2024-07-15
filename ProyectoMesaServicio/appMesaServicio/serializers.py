from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from appMesaServicio.models import *


class OficinaAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OficinaAmbiente
        fields = '__all__'


class TipoProcedimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProcedimiento
        fields = ('id', 'tipNombre', 'tipDescripcion',
                  'fechaHoraCreacion', 'fechaHoraActualizacion')


class UserSerializer(serializers.ModelSerializer):
    userFoto = Base64ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'userTipo', 'userFoto')
