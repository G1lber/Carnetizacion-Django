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

class Ficha(models.Model):
    num_ficha = models.IntegerField(primary_key=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True )

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_rol

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