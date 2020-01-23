from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import DjangoModelPermissions

from api.models import Application
from api.serializers import ApplicationSerializer


class ApplicationsAPIView(ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class SingleApplicationAPIView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class JSONApplicationAPIView(RetrieveAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    lookup_field = 'api_key'

