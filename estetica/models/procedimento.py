from django.db import models

class Procedimento(models.Model):
    nome = models.CharField(max_length=100)