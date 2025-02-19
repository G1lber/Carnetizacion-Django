from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('loginadmin/', views.loginAdmin, name="loginadmin"),
    path('iniciosuperusu/', views.inicio, name='inicio'),
    path('gestionarsuperusu/', views.gestionar, name='gestionar'),
    path('ficha/', views.ficha, name='ficha'),
    path('actualizarf/', views.actualizarf, name='actualizarf'),
    path('logout/', views.signout, name='logout'),
]