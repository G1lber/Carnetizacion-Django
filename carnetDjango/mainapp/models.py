from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.

class Rh(models.Model):
    nombre_tipo = models.CharField(max_length=3)
    def __str__(self):
        return self.nombre_tipo


class Tipo_doc(models.Model):
    nombre_doc = models.CharField(max_length=18)
    def __str__(self):
        return self.nombre_doc 

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_rol
 
class UsuarioPersonalizado(AbstractUser):
    documento = models.CharField(max_length=20, unique=True, blank=True, primary_key=True)
    # ficha = models.ForeignKey('Ficha', on_delete=models.SET_NULL, null=True, blank=True)
    rol_FK = models.ForeignKey('Rol', on_delete=models.SET_NULL, null=True, blank=True)
    rh_FK = models.ForeignKey('Rh', on_delete=models.SET_NULL, null=True, blank=True)
    tipo_doc_FK = models.ForeignKey('Tipo_doc', on_delete=models.SET_NULL, null=True, blank=True)
    is_active= models.IntegerField(default=True)
    foto = models.ImageField(upload_to='usuarios_fotos/', null=True, blank=True)

    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    def __str__(self):
        return self.username
    
class Ficha(models.Model):
    num_ficha = models.IntegerField(primary_key=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True )
    documento_user = models.ForeignKey('UsuarioPersonalizado', on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.BooleanField(default=True)

class FichaXaprendiz(models.Model):
    num_ficha_fk= models.ForeignKey('Ficha',on_delete=models.SET_NULL, null=True, blank=True)
    documento_fk= models.ForeignKey('UsuarioPersonalizado',on_delete=models.SET_NULL, null=True, blank=True)
    estadoC= models.BooleanField(default=False)

class Carnet(models.Model):
    documento_fk= models.ForeignKey('UsuarioPersonalizado',on_delete=models.SET_NULL, null=True, blank=True) 
    id_FichaXaprendiz= models.ForeignKey('FichaXaprendiz',on_delete=models.SET_NULL, null=True, blank=True)
    fecha_fin = models.DateField(blank=True, null=True )
    estado = models.BooleanField(default=True)  # Valor por defecto: True
