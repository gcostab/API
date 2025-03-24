from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario


class UsuarioForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = {'cpf', 'username', 'nome'}

class UsuarioEditForm(UserChangeForm):

    password = None
    
    class Meta:
        model = Usuario
        fields = {'cpf', 'username', 'nome'}