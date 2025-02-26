import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateFichaForms,CreatePersonalForm
from .models import Ficha, UsuarioPersonalizado, Tipo_doc, FichaXaprendiz, Rol, Rh
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

def gestionarC(request):
    return render(request,'mainapp/instru-gestionarA.html')


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
            ficha_instance = Ficha.objects.get(num_ficha=nueva_ficha.num_ficha)

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
                            user= UsuarioPersonalizado.objects.get(documento=row['Número de Documento'])
                            FichaXaprendiz.objects.create(
                                num_ficha_fk=ficha_instance,
                                documento_fk=user
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

def listar_aprendices(request):
    busqueda = request.GET.get("buscar", "")
    usuarios = UsuarioPersonalizado.objects.filter(rol_FK__nombre_rol="Aprendiz")  # Filtrar solo aprendices
    rh_list = Rh.objects.all()  # Obtener todos los RH

    if busqueda:
        usuarios = usuarios.filter(
            Q(first_name__icontains=busqueda) |
            Q(documento__icontains=busqueda)
        ).distinct()
        
    return render(request, 'mainapp/instru-gestionarA.html', {
        'usuarios': usuarios,
        'busqueda': busqueda,
        'rh_list': rh_list  # Pasar la lista de RH al template
    })

def editarAprendiz(request):
    if request.method == "POST":
        documento = request.POST.get("documento")
        rh_id = request.POST.get("rh")
        foto = request.FILES.get("foto")  # Obtener la foto si se subió

        usuario = get_object_or_404(UsuarioPersonalizado, documento=documento)
        usuario.rh_FK = get_object_or_404(Rh, id=rh_id)

        if foto:
            usuario.foto = foto  # Guardar la foto
            usuario.save()  # Guardar solo si la imagen cambia

        usuario.save()

        return JsonResponse({"success": True})

    return JsonResponse({"success": False, "error": "Método no permitido"}, status=400)
def personal(request):
    if request.method == 'POST':
        form = CreatePersonalForm(request.POST)
        print('llego el form')
        if form.is_valid():
            usuario = form.save(commit=False)  # No guarda aún en la base de datos
            usuario.is_active = True  # Activa el usuario por defecto
            print('hola')   
            rol = Rol.objects.get(nombre_rol=usuario.rol_FK) # Asumiendo que tienes un campo 'role'
            # Aquí puedes hacer lo que necesites dependiendo del rol
            if rol.nombre_rol == 'Funcionario':  # Si el rol es Funcionario
                usuario.set_password(usuario.password)  # Encripta la contraseña antes de guardarla
                usuario.save() 
            elif rol.nombre_rol == 'Instructor':  # Si el rol es manager
                usuario.username = usuario.documento # Un campo que tengas para manager
                usuario.password = usuario.documento 
                usuario.set_password(usuario.documento)
                usuario.save()  

                num_ficha = form.cleaned_data.get('ficha_field')  
                print(f"Ficha recibida del formulario: {num_ficha}")

                if num_ficha:
                    try:
                        # Verificar si existe una ficha con el num_ficha proporcionado
                        # ficha = Ficha.objects.get(num_ficha=num_ficha)  # Intentamos obtener la ficha por su número
                        # usuario.documento_user = usuario.documento  # Asignamos el usuario al campo documento_user
                        ficha=Ficha.objects.filter(num_ficha=num_ficha).update(documento_user=usuario.documento)
                        print(ficha)
                        
                        print('hola33333')
                    except Ficha.DoesNotExist:
                        print(f"No se encontró una ficha con el número {num_ficha}")
                        # Puedes manejar el error aquí (mostrar un mensaje o redirigir a una página de error)

                return redirect('personal')  # Redirigimos a la página correspondiente

            elif rol.nombre_rol == 'Aprendiz':  # Si el rol es manager
                usuario.username = usuario.documento # Un campo que tengas para manager
                usuario.save()

                num_ficha = form.cleaned_data.get('ficha_field') 
                if num_ficha:
                    try:
                        ficha_instance = Ficha.objects.get(num_ficha=num_ficha)
                        usuario_instance = UsuarioPersonalizado.objects.get(documento=usuario.documento)
                        fichaxA=FichaXaprendiz.objects.create(documento_fk=usuario_instance,num_ficha_fk=ficha_instance)
                        print(fichaxA)
                    except Ficha.DoesNotExist:
                        print(f"No se encontró una ficha con el número {num_ficha}")
                        # Puedes manejar el error aquí (mostrar un mensaje o redirigir a una página de error)

                return redirect('personal')  # Redirigimos a la página correspondiente
            else:
                usuario.is_active = True  
                return redirect('personal')
        else:
            form = CreatePersonalForm(request.POST)
            print(form.errors)

    else:
        form = CreatePersonalForm()
    print('holass')
    print(form.errors)
    return render(request, 'mainapp/super-gestionar.html', {
        'form': form  
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