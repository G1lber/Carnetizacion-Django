from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateFichaForms,CreatePersonalForm
from .models import Ficha, UsuarioPersonalizado
from django.db.models import Q
from django.http import JsonResponse




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
    return render(request,'mainapp/super-gestionar.html', {
        'form': CreatePersonalForm
        })

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
    busqueda = request.GET.get("buscar", "")
    fichas = Ficha.objects.all()

    if busqueda:
        fichas = fichas.filter(
            Q(num_ficha__icontains=busqueda) # Ajusta los campos según tu
        ).distinct()

    return render(request, 'mainapp/super-actualizar.html', {
        'fichas': fichas,
        'busqueda': busqueda

    })


#Views de Gestionar Personal
def listar_personal(request):
    busqueda = request.GET.get("buscar", "")  # Si no hay valor en GET, será una cadena vacía
    usuarios = UsuarioPersonalizado.objects.all()

    if busqueda:
        usuarios = usuarios.filter(
            Q(first_name__icontains=busqueda) |  # Filtrar solo si hay valor en busqueda
            Q(documento__icontains=busqueda)
        ).distinct()
        
    return render(request, 'mainapp/super-gestionar.html', {'usuarios': usuarios, 'busqueda': busqueda, 'form':CreatePersonalForm})

def personal(request):
    # Si el formulario se envía (POST)
    if request.method == 'POST':
        form = CreatePersonalForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario o la ficha
            return redirect('personal')  # Redirige a la misma página después de guardar
    else:
        form = CreatePersonalForm()  # Si la petición es GET, solo cargamos el formulario vacío

    return render(request, 'mainapp/super-gestionar.html', {
        'form': form  # Enviamos el formulario a la plantilla
    })

def signout(request):
    logout(request)
    return redirect('/loginadmin/')

def obtener_ficha(request, ficha_id):
    try:
        ficha = Ficha.objects.get(num_ficha=ficha_id)
        data = {
            "id": ficha.num_ficha,
            "fechaInicio": ficha.fecha_inicio,
            "fechaFin": ficha.fecha_fin,
            "estado": ficha.estado,
            # "codigo": ficha.codigo
        }
        return JsonResponse(data)
    except Ficha.DoesNotExist:
        return JsonResponse({"error": "Ficha no encontrada"}, status=404)
    
def editarficha(request):
    if request.method == "POST":
        ficha_id = request.POST.get("fichaId")  # Recuperar ID desde el formulario
        ficha = get_object_or_404(Ficha, pk=ficha_id)  # Buscar la ficha

        ficha.fecha_inicio = request.POST.get("fechaInicio")
        ficha.fecha_fin = request.POST.get("fechaFin")
        ficha.estado = request.POST.get("estado") == "on"  # Convertir checkbox a booleano
        ficha.save()

        return redirect('actualizarf')  # Redirigir después de guardar

    return redirect('actualizarf')  # Si no es POST, redirigir