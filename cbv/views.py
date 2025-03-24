from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from pessoa.models import Pessoa

# Create your views here.
class PessoaView(View):

    def get(self, request):

        return HttpResponse('Aqui é get!!!!')
    
    @method_decorator(csrf_exempt, name='dispatch')
    def post(self, request):

        return HttpResponse('Aqui é post!!!!')
    
class PessoaListView(ListView):
    model = Pessoa

class PessoaAddView(CreateView):
    model = Pessoa
    Fields = ['username', 'password', 'nome', 'idade', 'cpf',  'rg']
    template_name = 'pessoa/templates/pessoa/form.html'
    success_url = '/cbv/list/'
    

class PessoaEditView(UpdateView):
    model = Pessoa
    Fields = ['nome', 'idade', 'cpf',  'rg']
    success_url = '/cbv/list/'

class PessoaDelView(DeleteView):
    model = Pessoa
    success_url = '/cbv/list/'
    