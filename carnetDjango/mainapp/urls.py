from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="inicio"),
    path('loginadmin/', views.loginAdmin, name="loginadmin"),
    path('iniciosuperusu/', views.indexsuper, name='indexsuper'),
]