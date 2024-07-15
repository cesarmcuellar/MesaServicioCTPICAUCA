from appMesaServicio.models import *
from .views import generarPassword
# work
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from appMesaServicio.serializers import OficinaAmbienteSerializer, UserSerializer


class OficinaAmbienteList(generics.ListCreateAPIView):
    queryset = OficinaAmbiente.objects.all()
    serializer_class = OficinaAmbienteSerializer


class OficinaAmbienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OficinaAmbiente.objects.all()
    serializer_class = OficinaAmbienteSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OficinaAmbiente_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = OficinaAmbiente.objects.all()
        serializer = OficinaAmbienteSerializer(post, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OficinaAmbienteSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.ofiNombre)
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserApi(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            datosValidos = serializer.validated_data
            first_name = datosValidos['first_name']
            last_name = datosValidos['last_name']
            email = datosValidos['email']
            userTipo = datosValidos['userTipo']
            username = datosValidos['username']
            userFoto = datosValidos['userFoto']
            user = User(**datosValidos)
            user.save()
            passwordGenerado = generarPassword()
            print(f"password {passwordGenerado}")
            user.set_password(passwordGenerado)
            # se actualiza el user
            user.save()
            serializer_response = UserSerializer(user)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
