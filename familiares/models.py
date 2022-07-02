from django.db import models


class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    