from django.urls import path
from .views import home, autenticar, buscar_medicamento, despacho, recuperar_password, reportes, listar_usuarios_rol, crear_usuario, administrar_rol, listar_medicamentos, agregar_medicamento,modificar_medicamento

urlpatterns = [
    path('', home, name="home"),
    path('autenticar/', autenticar, name="autenticar"),
    path('buscar_medicamento/', buscar_medicamento, name="buscar_medicamento"),
    path('despacho/', despacho, name="despacho"),
    path('recuperar_password/', recuperar_password, name="recuperar_password"),
    path('reportes/', reportes, name="reportes"),
    path('listar_usuarios_rol/', listar_usuarios_rol, name="listar_usuarios_rol"),
    path('crear_usuario/', crear_usuario, name="crear_usuario"),
    path('administrar_rol/', administrar_rol, name="administrar_rol"),
    path('listar_medicamentos/', listar_medicamentos, name="listar_medicamentos"),
    path('agregar_medicamento/', agregar_medicamento, name="agregar_medicamento"),
    path('modificar_medicamento/', modificar_medicamento, name="modificar_medicamento"),
   
]
