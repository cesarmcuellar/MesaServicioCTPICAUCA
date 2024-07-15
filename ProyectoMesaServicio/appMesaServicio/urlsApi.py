from django.urls import path
from .apiViews import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('oficinaambiente/', OficinaAmbienteList.as_view()),
    path('oficinaambiente/<int:pk>/', OficinaAmbienteDetail.as_view()),
    path('usuario/', UserList.as_view()),
    path('usuario/<int:pk>/', UserDetail.as_view()),
    path('userApi/', UserApi.as_view()),
    path('oficina/', OficinaAmbiente_APIView.as_view()),
    path('docs/', include_docs_urls(title='Documentación API')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT
                          )
