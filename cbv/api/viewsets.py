from django.urls import path, include
from django.contrib.auth.models import User
from pessoa.models import Pessoa
from rest_framework import serializers, viewsets, routers
from cbv.api.serializer import PessoaSerializer

# Serializers define the API representation.

# ViewSets define the view behavior.
class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

