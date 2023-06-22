from django.db import models
import shortuuid


class URL(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=22, unique=True, default=shortuuid.uuid)

