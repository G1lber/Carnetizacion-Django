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
    path('ediaraprendiz/', views.editarAprendiz, name='editarAprendiz'),
    path('crearusu/', views.personal, name='crearusu'),
    path('logout/', views.signout, name='logout'),
    path('obtener-ficha/<int:ficha_id>/', views.obtener_ficha, name='obtener_ficha'),
    path('actualizar-usuario/', views.actualizar_usuario, name='actualizar_usuario'),
    path('eliminar_usuario/', views.eliminar_usuario, name='eliminar_usuario'),
    path('carnet/', views.obtener_datos_usuario_y_ficha, name='carnet'),
    
]