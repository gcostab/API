from pessoa.models import Pessoa
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import EmailField, IntegerField

class PessoaSerializer(ModelSerializer):

    contato_principal = EmailField(source='pessoa.email', required=False)
    total = IntegerField(min_value=1, max_value=99, required=False)
    class Meta:
        extra_kwargs = {
            'idade': {
                'write_only': True,
                'required': True
            },
            'email': {
                'write_only': True,
                'required': True
            },
            'contato_principal': {
                'write_only': True,
                'required': True
            }
        }
        model = Pessoa
        fields = ['id', 'username', 'nome', 'idade', 'cpf', 'email', 'contato_principal', 'total']