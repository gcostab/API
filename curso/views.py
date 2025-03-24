from django.shortcuts import render
from .models import Curso

# Create your views here.
def index(request):
    cursos = Curso.objects.all()

    context ={
        "curso": cursos
    }

    return render(request, "curso/index.html", context)