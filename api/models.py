import uuid

from django.db import models


class Application(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    api_key = models.CharField(max_length=100, unique=True, null=False, blank=True)

    def __str__(self):
        return f"{self.name}:{self.api_key}"

    def generate_api_key(self):
        self.api_key = uuid.uuid4()

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.generate_api_key()

        return super().save(*args, **kwargs)
