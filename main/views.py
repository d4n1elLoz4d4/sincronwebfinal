from http.client import HTTPResponse
from django.shortcuts import render,redirect
from .models import categoria, estadogestion, subcategoria, usuario, ServicioOfrecido, GestionCliente, Auditoria
from .forms import EstadoGestionForms, categoriaForms, subcategoriaForms, usuarioForms, ServicioOfrecidoForms, GestionClienteForms, AuditoriaForms
from django.contrib.auth.hashers import make_password
def inicio(request):
    
    context={
    }
    return render(request,'login.html',context)

def inicio(request):
    titulo='inicio'
    context={
        'titutlo':titulo,
    }
    return render(request,'index.html',context)

#vista EstadoGestion
def estadogestionview(request):
    titulo='gestion'
    context={
        'titutlo':titulo,
    }
    lista = estadogestion.objects.all()
    print(lista)
    return render(request,'gestion/estado_gestion.html',{'estados':lista})  

def creareg(request):
    lista = estadogestion.objects.all()
    formulario = EstadoGestionForms(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('estadogestion')
    return render(request,'generico/nuevo.html',{'formulario':formulario,'titulo':'Crear Estado Gestión','ListaEstados':lista, 'pagina':'estadogestion'}) 

def editarreg(request, id):
    gestion= estadogestion.objects.get(idEstadoGestion=id)
    formulario = EstadoGestionForms(request.POST or None, instance=gestion)
    lista = estadogestion.objects.all()
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('estadogestion')
    return render(request,'generico/editar.html',{'formulario':formulario, 'titulo':'Editar Estado Gestión','ListaEstados':lista,'pagina':'estadogestion' })

def eliminareg(request, id):
    estado = estadogestion.objects.get(idEstadoGestion = id)
    estado.delete()
    return redirect('estadogestion')

#vista Categorias
def categoriaview(request):
    titulo='categoria'
    context={
        'titutlo':titulo,
    }
    lista = categoria.objects.all()
    print(lista)
    return render(request,'categoria/categoria.html',{'ListaCategorias':lista})


def editarCategoria(request, id):
    item= categoria.objects.get(idCategoria=id)
    formulario = categoriaForms(request.POST or None, instance=item)
    lista = categoria.objects.all()
    vista = 'categoria'
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('categoria')
    return render(request,'generico/editar.html',{'formulario':formulario, 'titulo':'Editar Categoría','ListaEstados':lista,'pagina':'categoria'})

def eliminarCategoria(request, id):
    item = categoria.objects.get(idCategoria = id)
    item.delete()
    return redirect('categoria')

def crearcategoria(request):
    lista = categoria.objects.all()
    formulario = categoriaForms(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('categoria')
    return render(request,'generico/nuevo.html',{'formulario':formulario,'titulo':'Crear Categoría', 'ListaEstados':lista, 'pagina':'categoria'})    

        
#vista subcategoria
def subcategoriaview(request):
    titulo='subcategoria'
    context={
        'titutlo':titulo,
    }
    lista = subcategoria.objects.all()
    print(lista)
    return render(request,'subcategoria/subcategoria.html',{'ListasubCategorias':lista})


def editarsubCategoria(request, id):
    item= subcategoria.objects.get(idSubcategoria=id)
    formulario = subcategoriaForms(request.POST or None, instance=item)
    lista = subcategoria.objects.all()
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('subcategoria')
    return render(request,'generico/editar.html',{'formulario':formulario, 'titulo':'Editar subCategoría', 'ListaEstados':lista, 'pagina':'subcategoria'})

def eliminarsubCategoria(request, id):
    item = subcategoria.objects.get(idSubcategoria = id)
    item.delete()
    return redirect('subcategoria')

def crearsubcategoria(request):
    formulario = subcategoriaForms(request.POST or None)
    lista = subcategoria.objects.all()
    if formulario.is_valid():
        formulario.save()
        return redirect('subcategoria')
    return render(request,'generico/nuevo.html',{'formulario':formulario,'titulo':'Crear SubCategoría', 'ListaEstados':lista, 'pagina':'subcategoria'})

#vista usuario
def usuarioview(request):
    titulo='usuario'
    context={
        'titutlo':titulo,
    }
    lista = usuario.objects.all()
    print(lista)
    return render(request,'usuario/usuario.html',{'Listausuario':lista})


def editarusuario(request, id):
    item= usuario.objects.get(idUsuario=id)
    formulario = usuarioForms(request.POST or None, instance=item)
    lista = usuario.objects.all()
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('usuario')
    return render(request,'generico/editar.html',{'formulario':formulario, 'titulo':'Editar usuario','ListaEstados':lista,'pagina':'usuario'})

def eliminarusuario(request, id):
    item = usuario.objects.get(idUsuario = id)
    item.delete()
    return redirect('usuario')

def crearusuario(request):
    lista = usuario.objects.all()
    formulario = usuarioForms(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuario')
    return render(request,'generico/nuevo.html',{'formulario':formulario,'titulo':'Crear usuario','ListaEstados':lista, 'pagina':'usuario'})

#vista ServicioOfrecido
def ServicioOfrecidoview(request):
    titulo='ServicioOfrecido'
    context={
        'titutlo':titulo,
    }
    lista = ServicioOfrecido.objects.all()
    print(lista)
    return render(request,'ServicioOfrecido/ServicioOfrecido.html',{'ServicioOfrecido':lista})  

def crearServicioOfrecido(request):
    lista = ServicioOfrecido.objects.all()
    formulario = ServicioOfrecidoForms(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('ServicioOfrecido')
    return render(request,'generico/nuevo.html',{'formulario':formulario,'titulo':'Crear ServicioOfrecido', 'ListaEstados':lista, 'pagina':'ServicioOfrecido'}) 

def editarServicioOfrecido(request, id):
    item= ServicioOfrecido.objects.get(idServicioOfrecido=id)
    formulario = ServicioOfrecidoForms(request.POST or None, instance=item)
    lista = ServicioOfrecido.objects.all()
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('ServicioOfrecido')
    return render(request,'generico/editar.html',{'formulario':formulario, 'titulo':'Editar ServicioOfrecido', 'ListaEstados':lista, 'pagina':'ServicioOfrecido'})

def eliminarServicioOfrecido(request, id):
    item = ServicioOfrecido.objects.get(idServicioOfrecido = id)
    item.delete()
    return redirect('ServicioOfrecido')

    #vista GestionCliente
def GestionClienteview(request):
    titulo='GestionCliente'
    context={
        'titutlo':titulo,
    }
    lista = GestionCliente.objects.all()
    print(lista)
    return render(request,'GestionCliente/GestionCliente.html',{'GestionCliente':lista})  

def crearGestionCliente(request):
    lista = estadogestion.objects.all()
    formulario = GestionClienteForms(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('GestionCliente')
    return render(request,'generico/nuevo.html',{'formulario':formulario,'titulo':'Crear GestionCliente','ListaEstados':lista, 'pagina':'GestionCliente'}) 

def editarGestionCliente(request, id):
    item= GestionCliente.objects.get(idGestionCliente=id)
    formulario = GestionClienteForms(request.POST or None, instance=item)
    lista = estadogestion.objects.all()
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('GestionCliente')
    return render(request,'generico/editar.html',{'formulario':formulario, 'titulo':'Editar GestionCliente','ListaEstados':lista,'pagina':'GestionCliente'})

def eliminarGestionCliente(request, id):
    item = GestionCliente.objects.get(idGestionCliente = id)
    item.delete()
    return redirect('GestionCliente')

    #vista Auditoria
def Auditoriaview(request):
    titulo='Auditoria'
    context={
        'titutlo':titulo,
    }
    lista = Auditoria.objects.all()
    print(lista)
    return render(request,'Auditoria/Auditoria.html',{'Auditoria':lista})  

def crearAuditoria(request):
    lista = Auditoria.objects.all()
    formulario = AuditoriaForms(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Auditoria')
    return render(request,'generico/nuevo.html',{'formulario':formulario,'titulo':'Crear Auditoria','ListaEstados':lista, 'pagina':'Auditoria'}) 

def editarAuditoria(request, id):
    item= Auditoria.objects.get(idAuditoria=id)
    formulario = AuditoriaForms(request.POST or None, instance=item)
    lista = Auditoria.objects.all()
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Auditoria')
    return render(request,'generico/editar.html',{'formulario':formulario, 'titulo':'Editar Auditoria','ListaEstados':lista, 'pagina':'Auditoria'})

def eliminarAuditoria(request, id):
    item = Auditoria.objects.get(idAuditoria = id)
    item.delete()
    return redirect('Auditoria')
    
def loggedIn(request):
     if request.user.is_authenticated:
         respuesta:"Ingresado como "+ request.user.username
     else:
         respuesta:"No estas autenticado."
     return HttpResponse(respuesta)

def logout_user(request):

    return redirect('registration/login.html')
