from django.urls import path
from . import views
from .views import listar_personal
urlpatterns = [
    path('', views.index, name="index"),
    path('loginadmin/', views.loginAdmin, name="loginadmin"),
    path('iniciosuperusu/', views.inicio, name='inicio'),
    path('gestionarsuperusu/', views.gestionar, name='gestionar'),
    path('ficha/', views.ficha, name='ficha'),
    path('actualizarf/', views.actualizarf, name='actualizarf'),
    path('editarficha/', views.editarficha, name='editarficha'),
    path('personal/', views.listar_personal, name='personal'),
    path('crearusu/', views.personal, name='crearusu'),
    path('logout/', views.signout, name='logout'),
    path('obtener-ficha/<int:ficha_id>/', views.obtener_ficha, name='obtener_ficha'),
    path('carnet/', views.obtener_datos_usuario_y_ficha, name='carnet'),

    
]