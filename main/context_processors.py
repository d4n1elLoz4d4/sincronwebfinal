from usuarios.models import UsuarioLogin

def sesion(request):
    usuario_actual= request.user
    print("Hola")
    print(usuario_actual)
    image_user=r"../media/images/usuarios/default.png"
    context={
        'usuario_actual':usuario_actual,
        'image_user': image_user
    }
    return context