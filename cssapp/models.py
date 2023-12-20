from __future__ import unicode_literals

# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone


class Acta(models.Model):
    coordinador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    obra = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    texto = models.TextField()
    fecha = models.DateTimeField(
            default=timezone.now)
    firmacss = models.ImageField( null=True, blank=True, upload_to='firmacss/')
    firmacontrata = models.ImageField( null=True,blank=True, upload_to='firmacont/')

    def bd(self):
        self.save()

    def __str__(self):
        return self.obra