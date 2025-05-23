from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('loginadmin/', views.loginAdmin, name="loginadmin"),
    path('iniciosuperusu/', views.inicio, name='inicio'),
    path('gestionarsuperusu/', views.gestionar, name='gestionar'),
    path('gestionCarnet/', views.gestionarC, name='gestionarCarnet'),
    path('ficha/', views.ficha, name='ficha'),
    path('actualizarf/', views.actualizarf, name='actualizarf'),
    path('editarficha/', views.editarficha, name='editarficha'),
    path('personal/', views.listar_personal, name='personal'),
    path('fichasInstru/', views.listar_fichasA, name='buscarFichaInstr'),
    path('listarAprendiz/<int:num_ficha>/', views.listar_aprendices, name='listarAprendices'),
    path('cambiar_estado_aprendiz/', views.cambiar_estado_aprendiz, name='cambiar_estado_aprendiz'),
    path('editaraprendiz/', views.editarAprendiz, name='editarAprendiz'),
    path('crearusu/', views.personal, name='crearusu'),
    path('logout/', views.signout, name='logout'),
    path('logoutAprendiz/', views.signoutAprendiz, name='logoutAprendiz'),
    path('obtener-ficha/<int:ficha_id>/', views.obtener_ficha, name='obtener_ficha'),
    path('obtener-usuario/<int:user_id>/', views.obtener_usuario, name='obtener_usuario'),
    path('eliminar_usuario/', views.eliminar_usuario, name='eliminar_usuario'),
    path("actualizar-usuario/", views.actualizarUsuario, name="actualizar"),
    path('carnet/', views.obtener_datos_usuario_y_ficha, name='carnet'),
    path('informe/', views.informe, name='informe'),
    path('descargar-excel/', views.exportar_excel, name='descargar_excel'),
    
]