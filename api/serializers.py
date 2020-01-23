import logging

from rest_framework.serializers import ModelSerializer

from .models import Application

logger = logging.getLogger("api.serializers")


class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"
        read_only_fields = ("id", "api_key",)
