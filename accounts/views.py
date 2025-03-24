from django.shortcuts import render
from django.http import HttpResponse
from .forms import UsuarioForm, UsuarioEditForm
from django.contrib.auth.models import Group
from .models import Usuario

def createUser(request):
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Hello, world. You're at the accounts index.")
    else:
        form = UsuarioForm()
    
    return render(request, 'registration/login.html', {'form': form})

def editUser(request, user_id):

    user = Usuario.objects.get(pk=user_id)
    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)

            user.save()

            return HttpResponse('Usuário editado com sucesso')
        else:
            form = UsuarioForm()

        return render(request, 'registration/login.html', {'form': form})
    
