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
    path('personal/', views.listar_personal, name='listarpersonal'),
    path('logout/', views.signout, name='logout'),
    
]