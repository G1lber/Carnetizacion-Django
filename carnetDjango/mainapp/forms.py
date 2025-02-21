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