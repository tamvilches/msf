from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'app/home.html')

def autenticar(request):
    return render(request, 'app/autenticar.html')

def buscar_medicamento(request):
    return render(request, 'app/buscar_medicamento.html')

def despacho(request):
    return render(request, 'app/despacho.html')

def recuperar_password(request):
    return render(request, 'app/recuperar_password.html')

def reportes(request):
    return render(request, 'app/reportes.html')

def listar_usuarios_rol(request):
    return render(request, 'app/listar_usuarios_rol.html')

def crear_usuario(request):
    return render(request, 'app/crear_usuario.html')

def administrar_rol(request):
    return render(request, 'app/administrar_rol.html')

def listar_medicamentos(request):
    return render(request, 'app/listar_medicamentos.html')

def agregar_medicamento(request):
    return render(request, 'app/agregar_medicamento.html')

def modificar_medicamento(request):
    return render(request, 'app/modificar_medicamento.html')

