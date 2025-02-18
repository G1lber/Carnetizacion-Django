from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request,'mainapp/index.html')

def loginAdmin(request):
    if request.method == 'GET':
        print("Enviando formulario")
        return render(request, 'mainapp/loginadmin.html')
    else:
        print(request.POST)
        print('Obteniendo datos')
        user= authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'mainapp/loginadmin.html',{
                'error':'Usuario o Contraseña incorrecto'
            })
        else: 
            login(request, user)
            return redirect('indexsuper')
    
           

def indexsuper(request):
    return render(request,'mainapp/super-inicio.html')