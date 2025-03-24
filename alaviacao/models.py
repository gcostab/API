from django.db import models

# Create your models here.
class Avaliacao(models.Model):
    nota1 = models.FloatField()
    nota2 = models.FloatField()    
    notaFinal = models.FloatField()
    frequencia = models.IntegerField()
    turma = models.ForeignKey('turma.Turma', on_delete=models.CASCADE)
    aluno = models.ForeignKey('pessoa.Aluno', on_delete=models.CASCADE)