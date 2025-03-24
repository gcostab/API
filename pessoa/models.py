from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Classe Pessoa que pode ser Aluno ou Professor
class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200, default="Endereço padrão")
    telefone = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

# Aluno herda de Pessoa
class Aluno(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)  # Relacionamento correto
    matricula = models.CharField(max_length=200)
    situacao = models.CharField(max_length=200)

    def __str__(self):
        return f"Aluno: {self.pessoa.nome} - Matrícula: {self.matricula}"

# Professor herda de Pessoa
class Professor(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)  # Relacionamento correto
    titulacaoMaxima = models.CharField(max_length=200)

    def __str__(self):
        return f"Professor: {self.pessoa.nome} - Titulação: {self.titulacaoMaxima}"

# Licença para usuários
class License(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_key = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    valid_until = models.DateTimeField()

    def is_valid(self):
        """ Verifica se a licença ainda é válida """
        return self.is_active and self.valid_until >= timezone.now()

    def __str__(self):
        return f"{self.user.username} - License: {self.license_key}"
