from django.db import models

# Create your models here.
class Carros(models.Model):
    Nome_do_usuário_do_veículo = models.CharField(max_length=150)
    Placa_do_Carro = models.CharField(max_length=100)
    Marca_do_Carro = models.CharField(max_length=100)
    Ano_do_Carro = models.IntegerField(max_length=10)
    Cor_do_veículo = models.CharField(max_length=100)
    Número_do_RENAVAM = models.IntegerField(max_length=9)

