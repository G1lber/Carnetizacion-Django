from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.

class Rh(models.Model):
    A_POSITIVO ='A+'
    A_NEGATIVO ='A-'
    B_POSITIVO ='B+'
    B_NEGATIVO = 'B-'
    AB_POSITIVO ='AB+'
    AB_NEGATIVO ='AB-'
    O_POSITIVO ='O+'
    O_NEGATIVO = 'O-'

    NOMBRE_TIPO =[
        (A_POSITIVO,'A+'),
        (A_NEGATIVO,'A-'),
        (B_POSITIVO,'B+'),
        (B_NEGATIVO, 'B-'),
        (AB_POSITIVO,'AB+'),
        (AB_NEGATIVO,'AB-'),
        (O_POSITIVO,'O+'),
        (O_NEGATIVO, 'O-'),
    ]
    nombre_tipo = models.CharField(max_length=3, choices = NOMBRE_TIPO)

    def rh__(self):
        return self.nombre_tipo in {self. NOMBRE_TIPO}

class Tipo_doc(models.Model):
    CEDULA = 'CC'
    TARJETADEIDENTIDAD = 'TI'
    LIBRETAMILITAR = 'LM'
    CEDULAEXTRANJERA = 'CE'
    REGISTROCIVIL = 'RC'

    NOMBRE_DOC = [
        (CEDULA ,'CC'),
        (TARJETADEIDENTIDAD, 'TI'),
        (LIBRETAMILITAR, 'LM'),
        (CEDULAEXTRANJERA ,'CE'),
        (REGISTROCIVIL ,'RC'),
    ]
    nombre_doc = models.CharField(max_length=18, choices=NOMBRE_DOC)
    def tipodoc__(self):
        return self.nombre_doc in {self. NOMBRE_DOC}

class Ficha(models.Model):
    num_ficha = models.IntegerField(primary_key=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True )

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=100)

class UsuarioPersonalizado(AbstractUser):
    documento = models.CharField(max_length=20, unique=True, null=True, blank=True)
    ficha = models.ForeignKey('Ficha', on_delete=models.SET_NULL, null=True, blank=True)
    rol = models.ForeignKey('Rol', on_delete=models.SET_NULL, null=True, blank=True)
    rh = models.ForeignKey('Rh', on_delete=models.SET_NULL, null=True, blank=True)
    tipo_doc = models.ForeignKey('Tipo_doc', on_delete=models.SET_NULL, null=True, blank=True)

    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    def __str__(self):
        return self.username