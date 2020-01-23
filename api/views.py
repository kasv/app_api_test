from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import DjangoModelPermissions

from api.models import Application
from api.serializers import ApplicationSerializer


class ApplicationsAPIView(ListCreateAPIView):
    """ Получить список приложений или создать новое """
    authentication_classes = [BasicAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class SingleApplicationAPIView(RetrieveUpdateDestroyAPIView):
    """ Получить, обновить или удалить приложение по ID """
    authentication_classes = [BasicAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class JSONApplicationAPIView(RetrieveAPIView):
    """ Получить приложение по API ключу """
    authentication_classes = [BasicAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    lookup_field = 'api_key'

