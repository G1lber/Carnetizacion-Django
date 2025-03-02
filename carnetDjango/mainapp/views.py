import barcode
from barcode.writer import ImageWriter
from io import BytesIO
import base64
import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateFichaForms,CreatePersonalForm
from .models import Ficha, UsuarioPersonalizado, Tipo_doc, FichaXaprendiz, Rol, Rh
from django.db.models import Q
from django.http import JsonResponse
import json


# Create your views here.
def index(request):
    if request.method == "POST":
        documento = request.POST.get("documento")  # Obtener el número de documento

        try:
            usuario = UsuarioPersonalizado.objects.get(documento=documento)
            if usuario.rh_FK is not None and usuario.foto:
                request.session["documento"] = documento
                return redirect("carnet")  # Redirigir si cumple las condiciones
            else:
                return render(request, "mainapp/index.html", {"error": "El usuario no tiene RH o Foto asignados"})
        except UsuarioPersonalizado.DoesNotExist:
            return render(request, "mainapp/index.html", {"error": "Usuario no encontrado"})

    return render(request, "mainapp/index.html")

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
                return render(request,'mainapp/super-ficha.html', {
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
                    rol_instance = Rol.objects.get(id=1) 
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
                                    'rol_FK': rol_instance,
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

def listar_aprendices(request, num_ficha):
    # Obtener los documentos de los aprendices que pertenecen a la ficha
    aprendices_ficha = FichaXaprendiz.objects.filter(num_ficha_fk=num_ficha).values_list('documento_fk', flat=True)

    # Filtrar solo los usuarios que están en la ficha y que tienen el rol de "Aprendiz"
    usuarios = UsuarioPersonalizado.objects.filter(documento__in=aprendices_ficha, rol_FK__nombre_rol="Aprendiz")
    
    # Obtener la búsqueda del usuario
    busqueda = request.GET.get("buscar", "")
    usuarios2=''
    if busqueda:
        usuarios2 = usuarios.filter(
            Q(first_name__icontains=busqueda) |
            Q(documento__icontains=busqueda)
        ).distinct()

    # Obtener lista de RH
    rh_list = Rh.objects.all()

    return render(request, 'mainapp/instru-listarA.html', {
        'usuarios': usuarios,
        'usuarios2': usuarios2,
        'busqueda': busqueda,
        'ficha': num_ficha,
        'rh_list': rh_list
    })
def listar_fichasA(request):
    busqueda = request.GET.get("buscar", "")
    fichas = Ficha.objects.all()  # Filtrar solo aprendices
    rh_list = Rh.objects.all()  # Obtener todos los RH

    if busqueda:
        fichas = fichas.filter(
            Q(num_ficha__icontains=busqueda)
        ).distinct()
        
    return render(request, 'mainapp/instru-gestionarA.html', {
        'fichas': fichas,
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
    error2 = ""  # Asegurar que error2 esté definido siempre

    if request.method == 'POST':
        form = CreatePersonalForm(request.POST)

        if form.is_valid():
            documento = form.cleaned_data.get('documento')

            # Verificar si el documento ya existe
            if UsuarioPersonalizado.objects.filter(documento=documento).exists():
                error2 = "Error: El documento ya existe"
                return render(request, 'mainapp/super-gestionar.html', {'error2': error2})

            usuario = form.save(commit=False)  # No guarda aún en la base de datos
            usuario.is_active = True  # Activa el usuario por defecto
            
            rol = Rol.objects.get(nombre_rol=usuario.rol_FK)

            if rol.nombre_rol == 'Funcionario':
                usuario.set_password(usuario.password)
                usuario.save() 

            elif rol.nombre_rol == 'Instructor':
                usuario.username = usuario.documento
                usuario.password = usuario.documento
                usuario.set_password(usuario.documento)
                usuario.save()  

                num_ficha = form.cleaned_data.get('ficha_field')  
                if num_ficha:
                    ficha = Ficha.objects.filter(num_ficha=num_ficha).update(documento_user=usuario.documento)

            elif rol.nombre_rol == 'Aprendiz':
                usuario.username = usuario.documento
                usuario.save()

                num_ficha = form.cleaned_data.get('ficha_field')  
                if num_ficha:
                    try:
                        ficha_instance = Ficha.objects.get(num_ficha=num_ficha)
                        usuario_instance = UsuarioPersonalizado.objects.get(documento=usuario.documento)
                        fichaxA = FichaXaprendiz.objects.create(documento_fk=usuario_instance, num_ficha_fk=ficha_instance)
                    except Ficha.DoesNotExist:
                        print(f"No se encontró una ficha con el número {num_ficha}")

            return redirect('personal')

        else:
            error2 = "Error en el formulario. Verifica los datos ingresados."
            print("Errores en el formulario:", form.errors)

    else:
        form = CreatePersonalForm()

    return render(request, 'mainapp/super-gestionar.html', {'form': form, 'error2': error2})



def signout(request):
    logout(request)
    return redirect('/loginadmin/')

def signoutAprendiz(request):
    logout(request)
    return redirect('index')

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


def obtener_datos_usuario_y_ficha(request):
    documento = request.session.get("documento")  # Obtener documento desde la sesión

    if not documento:
        return redirect("index")  # Si no hay documento, redirigir al inicio

    usuario = get_object_or_404(UsuarioPersonalizado, documento=documento)
    ficha_x_aprendiz = FichaXaprendiz.objects.filter(documento_fk=usuario).first()
    fecha_vencimiento = ficha_x_aprendiz.num_ficha_fk.fecha_fin if ficha_x_aprendiz and ficha_x_aprendiz.num_ficha_fk else None

    # Usar Code 128 (o cualquier otro código de barras)
    codigo_barras = barcode.get_barcode_class('code128')  # Cambié 'ean13' a 'code128'
    codigo = codigo_barras(documento, writer=ImageWriter())

    # Guardar el código de barras en memoria
    buffer = BytesIO()
    codigo.write(buffer, options={'write_text': False, 'module_width': 0.3, 'module_height': 4})  # Esto oculta el número
    buffer.seek(0)

    # Convertir la imagen a base64
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Datos del usuario a pasar al template
    datos_usuario = {
        'first_name': usuario.first_name,
        'last_name': usuario.last_name,
        'documento': usuario.documento,
        'rh_FK': usuario.rh_FK.nombre_tipo if usuario.rh_FK else None,
        'tipo_doc_FK': usuario.tipo_doc_FK.nombre_doc if usuario.tipo_doc_FK else None,
        'rol_FK': usuario.rol_FK.nombre_rol if usuario.rol_FK else None,
        'num_ficha_fk': ficha_x_aprendiz.num_ficha_fk.num_ficha if ficha_x_aprendiz and ficha_x_aprendiz.num_ficha_fk else None,
        'fecha_vencimiento': fecha_vencimiento,
        'foto': usuario.foto,
        'barcode_base64': img_str,  # Imagen del código de barras en base64
    }

    # Renderizar el template con los datos
    return render(request, "mainapp/usu-carnet.html", {'datos': datos_usuario})

def obtener_usuario(request, user_id):
   
    if request.method == 'GET':
        usuario = get_object_or_404(UsuarioPersonalizado, documento=user_id)  # Busca el usuario por ID
        opciones = list(Rh.objects.values_list('id', 'nombre_tipo'))
        roles= list(Rol.objects.values_list('id', 'nombre_rol'))
        tipos= list(Tipo_doc.objects.values_list('id', 'nombre_doc'))

        # Devuelve los datos en formato JSON
        return JsonResponse({
            'documento': usuario.documento,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            'username': usuario.username,
            'email': usuario.email,
            'opcion_seleccionada': usuario.rh_FK.id if usuario.rh_FK else None,  # ID seleccionado
            'opciones': opciones,  # Lista de opciones disponibles
            'opcion_anterior': usuario.rol_FK.id if usuario.rol_FK else None,  # ID seleccionado
            'roles': roles,  # Lista de opciones disponibles
            'opcion_antes': usuario.tipo_doc_FK.id if usuario.tipo_doc_FK else None,  # ID seleccionado
            'tipos': tipos # Lista de opciones disponibles


        })
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def actualizarUsuario(request):
    if request.method == "POST":
        usuario_id = request.POST.get("documento")  # Recuperar ID desde el formulario
        usuario = UsuarioPersonalizado.objects.get(documento=usuario_id)
         

        #usuarios = get_object_or_404(Rh, pk=usuario_id)   Buscar la ficha
        usuario.first_name = request.POST.get("first_name")
        usuario.last_name = request.POST.get("last_name")
        usuario.email = request.POST.get("email")
        usuario.username = request.POST.get("username")

        nueva_password = request.POST.get("password")
        if nueva_password:  # Verifica si el campo no está vacío
            usuario.set_password(nueva_password)

        rh_id = request.POST.get("rh")
        usuario.rh_FK = Rh.objects.get(id=rh_id) if rh_id else None
        rol_id = request.POST.get("rol")
        usuario.rol_FK = Rol.objects.get(id=rol_id) if rol_id else None
        tipo_doc_id = request.POST.get("tipodoc")
        print(request.POST.get("tipodoc"))
        usuario.tipo_doc_FK = Tipo_doc.objects.get(id=tipo_doc_id) if tipo_doc_id else None
        usuario.save()

        return redirect('personal')  # Redirigir después de guardar

    return redirect('personal')  # Si no es POST, redirigir


def eliminar_usuario(request):
    if request.method == 'POST':
        documento = request.POST.get('documento')
        try:
            usuario = UsuarioPersonalizado.objects.get(documento=documento)
            usuario.delete()
            return JsonResponse({'success': True})
        except UsuarioPersonalizado.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Usuario no encontrado'})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

def informe(request):
    return render(request, 'mainapp/super-informe.html')