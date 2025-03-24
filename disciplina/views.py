from django.shortcuts import render
from .models import Disciplina
#from .forms import DisciplinaForm
#from django.shortcuts import redirect
#from django.contrib import 

# View que lista as minhas disiciplinas.
def index(request):
    disciplinas = Disciplina.objects.all()

    context ={
        "disciplina": disciplinas
    }

    return render(request, "disciplina/index.html", context)
# View que adiciona uma disciplina
def add(request):
    #if request.method()
    
    return render(request, "disciplina/add.html")