from django.db import models

# Create your models here.
# events/models.py
from django.db import models

class Categoria(models.Model):
    designacao = models.CharField(max_length=45)

class Localizacao(models.Model):
    localidade = models.CharField(max_length=45)
    rua = models.CharField(max_length=45)
    cod_postal = models.CharField(max_length=10)
    capacidade = models.IntegerField()

class Organizador(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=45)
    email = models.CharField(max_length=75)
    telemovel = models.CharField(max_length=20)

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    descricao = models.CharField(max_length=45)
    telemovel = models.CharField(max_length=20)

class Evento(models.Model):
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    gasto = models.DecimalField(max_digits=9, decimal_places=2)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.categoria} - {self.data_inicio}"