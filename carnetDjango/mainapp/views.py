from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateFichaForms
from .models import Ficha

# Create your views here.
def index(request):
    return render(request,'mainapp/index.html')

def loginAdmin(request):
    if request.method == 'GET':
        return render(request, 'mainapp/loginadmin.html')
    else:
        user= authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'mainapp/loginadmin.html',{
                'error':'Usuario o Contraseña incorrecto'
            })
        else: 
            login(request, user)
            return redirect('inicio')
    
           

def inicio(request):
    return render(request,'mainapp/super-inicio.html')

def gestionar(request):
    return render(request,'mainapp/super-gestionar.html')

def ficha(request):
    if request.method == 'GET':
        return render(request,'mainapp/super-ficha.html',{
            'form': CreateFichaForms
        })
    else:

        form =CreateFichaForms(request.POST)
        nueva_ficha= form.save(commit=False)
        nueva_ficha.save()
        return redirect('actualizarf')

def actualizarf(request):
    fichas=Ficha.objects.all()
    return render(request,'mainapp/super-actualizar.html',{
        'fichas':fichas
    })

# Esta views para cerrar la sesion
def signout(request):
    logout(request)
    return redirect('/loginadmin/')