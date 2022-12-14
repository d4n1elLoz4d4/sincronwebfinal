from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adm/',views.GestionClienteview,name='inicio-admin'),
    path('',auth_views.LoginView.as_view(),name='inicio'),

    #Gestión
    path('gestion/',views.estadogestionview,name='estadogestion'),
    path('gestion/nuevo',views.creareg,name='creaestado'),
    path('eliminar/<int:id>',views.eliminareg,name='eliminar'),
    path('gestion/editar/<int:id>',views.editarreg,name='editar'),

    #Categoría
    path('categoria/',views.categoriaview,name='categoria'),
    path('categoria/nuevo',views.crearcategoria,name='creacategoria'),
    path('categoria/editar/<int:id>',views.editarCategoria,name='editarCategoria'),
    path('eliminarCategoria/<int:id>',views.eliminarCategoria,name='eliminarCategoria'),

    #SubCategoría
    path('subcategoria/',views.subcategoriaview,name='subcategoria'),
    path('subcategoria/nuevo',views.crearsubcategoria,name='creasubcategoria'),
    path('subcategoria/editar/<int:id>',views.editarsubCategoria,name='editarsubCategoria'),
    path('eliminarsubCategoria/<int:id>',views.eliminarsubCategoria,name='eliminarsubCategoria'),

    #usuario
    path('usuario/',views.usuarioview,name='usuario'),
    path('usuario/nuevo',views.crearusuario,name='creausuario'),
    path('usuario/editar/<int:id>',views.editarusuario,name='editarusuario'),
    path('eliminarusuario/<int:id>',views.eliminarusuario,name='eliminarusuario'),
    path('usuarios/',include ('usuarios.urls')),

    #ServicioOfrecido
    path('ServicioOfrecido/',views.ServicioOfrecidoview,name='ServicioOfrecido'),
    path('ServicioOfrecido/nuevo',views.crearServicioOfrecido,name='creaServicioOfrecido'),
    path('ServicioOfrecido/editar/<int:id>',views.editarServicioOfrecido,name='editarServicioOfrecido'),
    path('eliminarServicioOfrecido/<int:id>',views.eliminarServicioOfrecido,name='eliminarServicioOfrecido'),

    #GestionCliente
    path('GestionCliente/',views.GestionClienteview,name='GestionCliente'),
    path('GestionCliente/nuevo',views.crearGestionCliente,name='creaGestionCliente'),
    path('GestionCliente/editar/<int:id>',views.editarGestionCliente,name='editarGestionCliente'),
    path('eliminarGestionCliente/<int:id>',views.eliminarGestionCliente,name='eliminarGestionCliente'),
    
    #Auditoria
    path('Auditoria/',views.Auditoriaview,name='Auditoria'),
    path('Auditoria/nuevo',views.crearAuditoria,name='creaAuditoria'),
    path('Auditoria/editar/<int:id>',views.editarAuditoria,name='editarAuditoria'),
    path('eliminarAuditoria/<int:id>',views.eliminarAuditoria,name='eliminarAuditoria'),





]