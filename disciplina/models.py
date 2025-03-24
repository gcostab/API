from django.db import models
import uuid
# Create your models here.

class Disciplina(models.Model):
    codigo = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    descricao = models.CharField(max_length=200)
    cargaHoraria = models.IntegerField()
    ementa = models.TextField()
    bibliografia = models.TextField()

    #Fruto da relação de muitos para muitos
    preRequisito = models.ManyToManyField("self", blank=True, symmetrical=False)

    def __str__(self):
        return self.descricao