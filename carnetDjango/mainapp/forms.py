from django.forms import ModelForm
from .models import Ficha, UsuarioPersonalizado

class CreateFichaForms(ModelForm):
    class Meta:
        model= Ficha
        fields = ['num_ficha','fecha_inicio','fecha_fin','documento_user']