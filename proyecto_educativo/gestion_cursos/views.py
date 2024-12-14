from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm

# Página de inicio
def index(request):
    return render(request, 'gestion_cursos/index.html')

# Lista de cursos
def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'gestion_cursos/lista_cursos.html', {'cursos': cursos})

# Crear un nuevo curso
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'gestion_cursos/crear_curso.html', {'form': form})