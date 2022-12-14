from django import forms
from .models import categoria, estadogestion, subcategoria, usuario, ServicioOfrecido, GestionCliente, Auditoria

class EstadoGestionForms(forms.ModelForm):
    class Meta:
        model = estadogestion
        fields='__all__'

class categoriaForms(forms.ModelForm):
    class Meta:
        model = categoria
        fields='__all__'        

class subcategoriaForms(forms.ModelForm):
    class Meta:
        model = subcategoria
        fields='__all__'            


class usuarioForms(forms.ModelForm):
    class Meta:
        model = usuario
        fields='__all__'                    

class ServicioOfrecidoForms(forms.ModelForm):
    class Meta:
        model = ServicioOfrecido
        fields='__all__'                    
       

class GestionClienteForms(forms.ModelForm):
    class Meta:
        model = GestionCliente
        fields='__all__'        

        
class AuditoriaForms(forms.ModelForm):
    class Meta:
        model = Auditoria
        fields='__all__'        