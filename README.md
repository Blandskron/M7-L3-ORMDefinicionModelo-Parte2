# Nuevo Proyecto Django: Sistema de Gestión de Cursos

En este proyecto, implementaremos un sistema educativo que gestiona **cursos** en lugar de estudiantes. Esto permitirá demostrar la misma funcionalidad pero con un enfoque diferente, utilizando Django y PostgreSQL.

## 1. Crear la Aplicación: `gestion_cursos`

Primero, crearemos la aplicación `gestion_cursos`:

```bash
python manage.py startapp gestion_cursos
```

Agregamos la aplicación al archivo `settings.py` en la sección `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'gestion_cursos',
]
```

---

## 2. Definir el Modelo: `models.py`

Archivo: `gestion_cursos/models.py`

```python
from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_horas = models.PositiveIntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre
```

- **`nombre`**: Nombre del curso.
- **`descripcion`**: Descripción detallada del curso.
- **`duracion_horas`**: Duración en horas del curso.
- **`fecha_inicio`** y **`fecha_fin`**: Fechas de inicio y finalización del curso.

Realizamos las migraciones:

```bash
python manage.py makemigrations gestion_cursos
python manage.py migrate
```

---

## 3. Crear Formulario: `forms.py`

Archivo: `gestion_cursos/forms.py`

```python
from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'duracion_horas', 'fecha_inicio', 'fecha_fin']
```

Este formulario permitirá la entrada de datos del modelo `Curso`.

---

## 4. Crear las Vistas: `views.py`

Archivo: `gestion_cursos/views.py`

```python
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
```

---

## 5. Definir las URLs: `urls.py`

Archivo: `gestion_cursos/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/nuevo/', views.crear_curso, name='crear_curso'),
]
```

Agrega las rutas al archivo principal `urls.py` del proyecto:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion_cursos.urls')),
]
```

---

## 6. Crear las Plantillas HTML

#### Crear Directorio de Plantillas
Crea la carpeta `templates/gestion_cursos` dentro de la aplicación `gestion_cursos`.

---

### **Plantilla `index.html`**

Archivo: `gestion_cursos/templates/gestion_cursos/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página de Inicio</title>
</head>
<body>
    <h1>Bienvenido al Sistema de Gestión de Cursos</h1>
    <nav>
        <ul>
            <li><a href="{% url 'lista_cursos' %}">Lista de Cursos</a></li>
            <li><a href="{% url 'crear_curso' %}">Registrar Curso</a></li>
        </ul>
    </nav>
</body>
</html>
```

---

### **Plantilla `lista_cursos.html`**

Archivo: `gestion_cursos/templates/gestion_cursos/lista_cursos.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Cursos</title>
</head>
<body>
    <h1>Lista de Cursos</h1>
    <table border="1">
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Descripción</th>
                <th>Duración (horas)</th>
                <th>Fecha Inicio</th>
                <th>Fecha Fin</th>
            </tr>
        </thead>
        <tbody>
            {% for curso in cursos %}
                <tr>
                    <td>{{ curso.nombre }}</td>
                    <td>{{ curso.descripcion }}</td>
                    <td>{{ curso.duracion_horas }}</td>
                    <td>{{ curso.fecha_inicio }}</td>
                    <td>{{ curso.fecha_fin }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
    <a href="{% url 'crear_curso' %}">Registrar Nuevo Curso</a>
</body>
</html>
```

---

### **Plantilla `crear_curso.html`**

Archivo: `gestion_cursos/templates/gestion_cursos/crear_curso.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registrar Curso</title>
</head>
<body>
    <h1>Registrar Curso</h1>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Guardar</button>
    </form>
    <a href="{% url 'lista_cursos' %}">Volver a la Lista</a>
</body>
</html>
```

---

## 7. Ejecutar el Servidor

```bash
python manage.py runserver
```

Accede a:

- Página de inicio: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Lista de cursos: [http://127.0.0.1:8000/cursos/](http://127.0.0.1:8000/cursos/)
- Registrar curso: [http://127.0.0.1:8000/cursos/nuevo/](http://127.0.0.1:8000/cursos/nuevo/)

---

Este sistema implementa la misma lógica que el proyecto anterior, pero aplicado a cursos. ¡Avísame si necesitas más ampliaciones!
