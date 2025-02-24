from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateFichaForms,CreatePersonalForm
from .models import Ficha, UsuarioPersonalizado
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
        return render(request,'mainapp/super-ficha.html',{
            'form': CreateFichaForms
        })
    else:
        form =CreateFichaForms(request.POST)
        nueva_ficha= form.save(commit=False)
        nueva_ficha.save()
        archivo_excel= request.FILES.getlist('archivo_excel')

        if not archivo_excel:
            return redirect('templates/super-ficha.html')
        
        for archivo in archivo_excel:
                    nueva_ficha = Ficha(
                        num_ficha=int( num_ficha),
                        fecha_inicio=fecha_inicio,
                        fecha_fin=fecha_fin,
                        archivo_excel=archivo,
                    )
                    nueva_ficha.save()

                    procesar_excel(nueva_ficha)

        except Exception as e:
            print(f"Error: {e}")  # Para depuración

        return redirect('actualizarf')

def procesar_excel(ficha):
    try:
        df = pd.read_excel(ficha.archivo_excel.path, engine="openpyxl", skiprows=5)
        print(df.head())  # Muestra las primeras filas para revisar si están correctas

        if df.empty:
            return

        df = pd.read_excel(ficha.archivo_excel.path, engine="openpyxl", skiprows=5, usecols="A,B,C,D,G")
        df.columns = ["documento_user", "nombre_usuario", "apellido_usuario", "estado"]


        for _, row in df.iterrows():
            if pd.notna(row["documento_user"]):
                print(f"Procesando usuario: {row['documento_user']} - {row['nombre_usuario']} {row['apellido_usuario']}")

                try:
                    tipo_doc, _ = TipoDoc.objects.get_or_create(nombre_tipoD=row["tipo_doc_FK"])
                    estado, _ = Estado.objects.get_or_create(nombre_estado=row["estado"])

                    usuario, created = UsuarioPersonalizado.objects.update_or_create(
                        documento=row["documento"],
                        defaults={
                            "first_name": row["nombre_usuario"],
                            "last_name": row["apellido_usuario"],
                            "tipo_doc_FK": tipo_doc,
                            # "id_ficha_FK": ficha,
                            # "id_programa_FK": ficha.programa
                            # "id_estado_FK": estado,
                        },
                    )
                except Exception:
                    pass
    except Exception:
        pass

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