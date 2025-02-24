import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateFichaForms,CreatePersonalForm
from .models import Ficha, UsuarioPersonalizado, Tipo_doc
from django.db.models import Q



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
        return render(request, 'mainapp/super-ficha.html', {
            'form': CreateFichaForms
        })
    else:
        form = CreateFichaForms(request.POST)
        if form.is_valid():
            nueva_ficha = form.save(commit=False)
            nueva_ficha.save()

            # Procesar el archivo Excel
            archivo_excel = request.FILES.get('archivo_excel')
            if not archivo_excel:
                return render(request, 'mainapp/super-ficha.html', {
                    'form': form,
                    'error': "No se cargó el archivo Excel."
                })
            else:
                try:
                    # Leer el archivo Excel, omitiendo las primeras 10 filas
                    df = pd.read_excel(archivo_excel, skiprows=9)

                    # Verificar que el archivo tenga las columnas esperadas
                    expected_columns = ['Tipo de Documento', 'Número de Documento', 'Nombre', 'Apellidos', 'Estado']
                    if not all(col in df.columns for col in expected_columns):
                        return render(request, 'mainapp/super-ficha.html', {
                            'form': form,
                            'error': "El archivo Excel no tiene las columnas esperadas."
                        })

                    # Iterar sobre las filas del DataFrame
                    for index, row in df.iterrows():
                        # Obtener la instancia de Tipo_doc
                        try:
                            tipo_doc_instance = Tipo_doc.objects.get(nombre_doc=row['Tipo de Documento'])  # Asegúrate de que 'id' sea el campo correcto
                            if row['Estado'] != "EN FORMACION":
                                is_active = 0
                            else:
                                is_active= 1
                            # Crear o actualizar el usuario
                            user, creado = UsuarioPersonalizado.objects.update_or_create(
                                documento=row['Número de Documento'],
                                defaults={
                                    'tipo_doc_FK': tipo_doc_instance,
                                    'username':row['Número de Documento'],
                                    'documento': row['Número de Documento'],
                                    'first_name': row['Nombre'],
                                    'last_name': row['Apellidos'],
                                    'is_active': is_active
                                }
                            )

                        except Tipo_doc.DoesNotExist:
                            return render(request, 'mainapp/super-ficha.html', {
                                'form': form,
                                'error': f"No se encontró el Tipo_doc con ID {row['tipo_doc_FK']}."
                            })

                    # Redirigir una vez que todo se haya procesado
                    return redirect('personal')

                except Exception as e:
                    return render(request, 'mainapp/super-ficha.html', {
                        'form': form,
                        'error': f"Error al leer el archivo Excel: {str(e)}"
                    })
        else:
            print(form.errors)
            return render(request, 'mainapp/super-ficha.html', {
                'form': form,
                'error': form.errors
            })



def actualizarf(request):
    fichas= Ficha.objects.all()
    return render(request,'mainapp/super-actualizar.html',{
        'fichas':fichas
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