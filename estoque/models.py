from django.db import models
from django.contrib.auth.models import User

class Local(models.Model):
    nome = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Locais'

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Fabricante(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Componente(models.Model):
    nome = models.CharField(max_length=200)
    quantidade = models.PositiveIntegerField(default=0)
    aplicacao = models.CharField(max_length=200)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Log(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    horario = models.DateTimeField(auto_now_add=True)
