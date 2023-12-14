from django.db import models

# Create your models here.

class Usuarios(models.Model):
    cpf = models.CharField(max_length=11, unique=True, primary_key=True)
    nome = models.CharField(max_length=150, blank=False, null=False)
    email = models.CharField(max_length=150, blank=False, null=False)
    senha = models.CharField(max_length=150, blank=False, null=False)
    c_permissao = models.BooleanField(default=False, blank=True, null=True)
    g_permissao = models.BooleanField(default=False, blank=True, null=True)
    nome_cartao = models.CharField(max_length=150, blank=True, null=True)
    numero_cartao = models.CharField(max_length=150, blank=True, null=True)
    vencimento_cartao = models.CharField(max_length=150, blank=True, null=True)
    cvc_cartao = models.CharField(max_length=3, blank=True, null=True)

class Viagem(models.Model):
    data = models.CharField(max_length=150, blank=False, null=False)
    origem = models.CharField(max_length=150, blank=False, null=False)
    destino = models.CharField(max_length=150, blank=False, null=False)

class Passagems(models.Model):
    valor = models.CharField(max_length=150, blank=False, null=False)
    id_viagem = models.ForeignKey(Viagem, on_delete=models.CASCADE)
    cpf_passageiro = models.ForeignKey(Usuarios, on_delete=models.CASCADE) 