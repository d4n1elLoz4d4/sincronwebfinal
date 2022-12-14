from django.db import models
from django.contrib.auth.models import User

class estadogestion(models.Model):
    idEstadoGestion = models.AutoField(primary_key=True)
    estadoGestionNombre = models.CharField(max_length= 45,verbose_name='Nombre')
    estadoGestionDescripcion = models.CharField(max_length= 125,verbose_name='Descripción')
    estadoGestionActivo = models.CharField(max_length= 1,verbose_name='Estado')

class categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    categoriaDescripcion = models.CharField(max_length= 45,verbose_name='Descripción')
    categoriaActivo = models.CharField(max_length= 1,verbose_name='Estado')


class subcategoria(models.Model):
    idSubcategoria = models.AutoField(primary_key=True)
    subcategoriaDescripcion = models.CharField(max_length= 45,verbose_name='Descripción')
    subcategoriaActivo = models.CharField(max_length= 1,verbose_name='Estado') 
    Categoria_idCategoria = models.IntegerField(verbose_name='Categoria')

class usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    usuarioNombre = models.CharField(max_length= 45,verbose_name='Nombre')
    usuarioApellido = models.CharField(max_length= 45,verbose_name='Apellido')
    usuarioTipoDocumento = models.CharField(max_length= 45,verbose_name='Tipo de Documento', blank=False, null=False)
    usuarioNumeroDocumento = models.IntegerField(verbose_name='Numero de Documento', blank=False, null=False)
    usuarioClave = models.CharField(max_length= 45,verbose_name='Contraseña')
    usuarioCorreo = models.CharField(max_length= 65,verbose_name='Correo', blank=False, null=False)
    usuarioRol = models.CharField(max_length= 45,verbose_name='Rol usuario')
    usuarioActivo = models.CharField(max_length= 1,verbose_name='Estado', blank=True, null=False)
    email= models.EmailField(max_length=150, verbose_name='Correo', default='-')
    
class ServicioOfrecido(models.Model):
    idServicioOfrecido = models.AutoField(primary_key=True)
    servicioOfrecidoNombre = models.CharField(max_length= 45,verbose_name='Nombre')
    servicioOfrecidoDesripcion = models.CharField(max_length= 125,verbose_name='Descripción')
    servicioOfrecidoActivo = models.CharField(max_length= 1,verbose_name='Estado')

class GestionCliente(models.Model):
    idGestionCliente = models.AutoField(primary_key=True)
    gestionClienteRegistro = models.DateTimeField(verbose_name='Fecha de Registro')
    gestionClienteObservacion = models.CharField(max_length= 254,verbose_name='Observacion',blank=True, null=False)
    gestionClienteTiempoInvertido = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Tiempo', blank=True, null=False)
    EstadoGestion_idEstadoGestion = models.IntegerField(verbose_name='Estado')
    Subcategoria_idSubcategoria = models.IntegerField(verbose_name='Subcategoria')
    Usuario_idUsuario = models.IntegerField(verbose_name='Usuario')
    Cliente_idGestionCliente = models.IntegerField(verbose_name='Cliente')

class Auditoria(models.Model):
    idAuditoria = models.AutoField(primary_key=True)
    auditoriaNombre = models.CharField(max_length= 45,verbose_name='Nombre')
    auditoriaDescripcion = models.CharField(max_length= 255,verbose_name='Descripción')
    auditoriaRegistro = models.DateTimeField(verbose_name='Fecha de Registro')
    Usuario_idUsuario = models.IntegerField(verbose_name='Usuario')
    GestionCliente_idGestionCliente = models.IntegerField(max_length= 11,verbose_name='Estado')