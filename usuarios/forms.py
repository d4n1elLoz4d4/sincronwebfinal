from django.forms import ModelForm, widgets
from usuarios.models import UsuarioLogin

class UsuarioForm(ModelForm):
    class Meta:
        model= UsuarioLogin
        exclude=['estado','user']
        widgets={
            'fecha_nacimiento': widgets.DateInput(attrs={'type':'date'})
        }
