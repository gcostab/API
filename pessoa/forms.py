from django.forms import ModelForm
from .models import Pessoa
from django.forms import TextInput

class PessoaForm(ModelForm):
    class Meta():
        model =  Pessoa
        fields = {'nome'}
        widgets = {
            'nome' : TextInput(attrs={
                'class' : 'form-control form-control-user'}),
        }
    
    def save(self, commit=True):
        print("Veio salvar!")
        pessoa = super(PessoaForm, self).save(commit=False)
        pessoa.set.password(self.cleaned_data('password'))
        if commit:
            pessoa.save()
        return pessoa