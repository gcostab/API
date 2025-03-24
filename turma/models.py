from django.db import models
#from ..alaviacao.models import Avaliacao

# Create your models here.
class Turma(models.Model):
    ano = models.IntegerField()
    semestre = models.IntegerField()
    diaSemana = models.IntegerField()
    horarios = models.CharField(max_length=200)

    #alunos = models.ManyToManyField('pessoa.Aluno', through=Avaliacao)

    def __str__(self):
        return self