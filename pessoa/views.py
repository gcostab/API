from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Pessoa
from .forms import PessoaForm
from django.contrib.auth.decorators import login_required

#create
@login_required
def add(request):

    if request.method == "POST":
        form = PessoaForm(request.POST)
        #if form.is_valid():
        form.save()
        return HttpResponseRedirect('/pessoa/')
    else:
        form = PessoaForm()
    return render(request, 'pessoa/add.html', {'form': form})

#read
@login_required
def lista (request):

    if request.GET:
    
        dic = {}

        for key, val in request.GET.lists():
            dic.update({key:val[0]})
        pessoas = Pessoa.objects.all().filter(**dic)
    else:
        #Aciono o Model Pessoa
        pessoas = Pessoa.objects.all()

    context = { 'pessoas' : pessoas }
    #Responder ao meu inimigo(usuário)
    return render(request, "pessoa/index.html", context)


def detail(request, pessoa_id):
#pk = primary key
    #recupera a pessoa do id passado pelo parametro
    pessoa = Pessoa.objects.get(pk=pessoa_id)

    html = "<ul>"
    html += "<li> ID: " + str(pessoa.id) + "</li>"
    html += "<li> Nome: " + pessoa.nome + "</li>"
    html += "<li> Idade: " + str(pessoa.idade) + "</li>"
    html += "<li> Cpf: " + pessoa.cpf + "</li>"
    html += "<li> Rg: " + pessoa.rg + "</li>"
    html += "</ul>"

    html += "<a href='/pessoa/'> Voltar </a>" 

    return HttpResponse(html)

#update
def edit(request, pessoa_id):
    pessoa = Pessoa.objects.get(pk=pessoa_id)

    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pessoa/')
    else:
        form = PessoaForm(instance=pessoa)

    return render(request, 'pessoa/edit.html', {'form': form})

#delete
def remove(request, pessoa_id):
    pessoa = Pessoa.objects.get(pk=pessoa_id).delete()

    return HttpResponseRedirect('/pessoa/')


#filter_cpf
def filterCpf(request, query):
# O __contains funciona como o LIKE e só funciona com string
    pessoas = Pessoa.objects.all().filter(cpf__contains=query)
    html = "<table border = '1'>"
    for pessoa in pessoas :
        html += "<tr>"
        html += "<td>" + str(pessoa.id) + "</td>"
        html += "<td>" + pessoa.nome + "</td>" 
        html += "<td>" + str(pessoa.idade) + "</td>" 
        html += "<td>" + pessoa.cpf + "</td>" 
        html += "<td> <a href='/pessoa/"+ str(pessoa.id) +"/'> Ver detalhes </a> </td>" 
        html += "</tr>" 
    html += "</table>"
    return HttpResponse(html)

def license_invalid(request):
    return render(request, 'license_invalid.html', {})

def license_missing(request):
    return render(request, 'license_missing.html', {})