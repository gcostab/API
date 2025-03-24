from django.db import models
from disciplina.models import Disciplina
import uuid
# Create your models here.

class Curso(Disciplina):
    codigo1 = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    descricao1 = models.CharField(max_length=200)