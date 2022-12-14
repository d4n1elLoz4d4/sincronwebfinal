from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class UsuarioLogin(models.Model):
    nombres=models.CharField(max_length=60, verbose_name="Nombres")
    apellidos=models.CharField(max_length=60, verbose_name="Apellidos")
    foto=models.ImageField(upload_to='images/usuarios',blank=True, default='images/usuarios/default.png')
    email= models.EmailField(max_length=150, verbose_name='Correo', default='-')

    class TipoDocumento(models.TextChoices):
        CC='C.C', _('Cédula de Ciudadanía')
        CE='C.E', _('Cédula de Extranjería')
        TI='T.I', _('Tarjeta de Identidad')
        OT='Otro', _('Otro Tipo de Documento')
    tipoDocumento=models.CharField(max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    documento=models.CharField(max_length=50, verbose_name="Número de Documento")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")
    fecha_nacimiento=models.DateField(verbose_name="Fecha de Nacimiento", help_text=u"MM/DD/AAAA")

    class Rol(models.TextChoices):
        Administrador='Administrador', _('Administrador')
        Empleado='Empleado', _('Empleado')
        Cliente='Cliente', _('Cliente')
        Proveedor='Proveedor', _('Proveedor')
    rol=models.CharField(max_length=13, choices=Rol.choices, default=Rol.Empleado, verbose_name="Rol")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    user=models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self)->str:
        return "%s %s" %(self.nombres, self.apellidos) 
   