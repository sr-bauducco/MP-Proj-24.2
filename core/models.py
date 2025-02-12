from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    TIPO_USUARIO = [
        ('admin', 'Administrador'),
        ('feirante', 'Feirante'),
        ('comprador', 'Comprador'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_USUARIO, default='comprador')


class Banca(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    dono = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'tipo': 'feirante'})

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    banca = models.ForeignKey(Banca, on_delete=models.CASCADE, related_name='produtos')

    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"
    
class Avaliacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='avaliacoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.PositiveIntegerField()
    comentario = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação de {self.usuario} para {self.produto}"
    
class MensagemPrivada(models.Model):
    remetente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensagens_enviadas')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensagens_recebidas')
    conteudo = models.TextField()
    enviado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De {self.remetente} para {self.destinatario}"
    
class Relatorio(models.Model):
    data_geracao = models.DateTimeField(auto_now_add=True)
    total_usuarios = models.IntegerField()
    total_pesquisas = models.IntegerField()
    top_produtos = models.TextField()
    top_bancas = models.TextField()


class Feira(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.nome
