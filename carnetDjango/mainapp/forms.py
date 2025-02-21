from django.forms import ModelForm
from .models import Ficha, UsuarioPersonalizado
from django import forms

class CreateFichaForms(ModelForm):
    class Meta:
        model= Ficha
        fields = ['num_ficha','fecha_inicio','fecha_fin','documento_user']
        widgets = {
            'num_ficha': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de ficha'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'documento_user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Documento de usuario'}),
        }

class CreatePersonalForm(ModelForm):
    class Meta:
        model= UsuarioPersonalizado
        fields = ['first_name','last_name','documento','tipo_doc','rol','username','email','password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'documento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de Documento'}),
            'tipo_doc': forms.Select(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        }