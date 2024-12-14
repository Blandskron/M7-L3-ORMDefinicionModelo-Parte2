from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/nuevo/', views.crear_curso, name='crear_curso'),
]