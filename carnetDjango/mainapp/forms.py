from django.forms import ModelForm
from .models import Ficha, UsuarioPersonalizado
from django import forms

class CreateFichaForms(ModelForm):
    
    class Meta:
        model= Ficha
        fields = ['num_ficha','fecha_inicio','fecha_fin','documento_user','estado']
        widgets = {
            'num_ficha': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de ficha'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'documento_user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Documento de usuario'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-control'}),

        }

class CreatePersonalForm(ModelForm):
    username=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
        required=False)
    email=forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}),
        required=False)
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        required=False)
    class Meta:
        model= UsuarioPersonalizado
        fields = ['first_name','last_name','documento','tipo_doc_FK','rol_FK','username','email','password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'documento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de Documento'}),
            'tipo_doc_FK': forms.Select(attrs={'class': 'form-control'}),
            'rol_FK': forms.Select(attrs={'class': 'form-control'}),
            # 'is_active': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado'}),
        }
   