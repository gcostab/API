from django import forms
from .models import Disciplina


class DisciplinaForm(forms.ModelForm):

    preRequisito = forms.ModelMultipleChoiceField(
        queryset=Disciplina.objects.all().exclude(descricao__endwith(" A"))  # type: ignore
        )

    terms = forms.BooleanField(required=True, label="Aceite os termos de uso*")

    class Meta:
        model = Disciplina
        fields = '__all__'
        widgets = {
            'pre-requisito' : forms.CheckboxSelectMultiple(attrs={'class': 'form.check-input'})
        }
        labels = {
            "preRequisito": "Pré-requisitos"
        }
        help_texts = {
            "preRequisito": "Selecione os pré-requisitos da disciplina." 
        }