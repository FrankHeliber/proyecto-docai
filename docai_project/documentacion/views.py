from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Artefacto, EvaluacionCoherencia
from .forms import ProjectForm, ArtefactoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from core.ia import generar_artefacto_con_ia

@login_required
def dashboard(request):
    proyectos = Project.objects.filter(propietario=request.user)
    return render(request, 'documentacion/dashboard.html', {'proyectos': proyectos})

def crear_proyecto(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.propietario = request.user  # Asume que el usuario está logueado
            proyecto.save()
            return redirect('lista_proyectos')  # Cambia según el nombre de tu vista/lista
    else:
        form = ProjectForm()
    return render(request, 'documentacion/crear_proyecto.html', {'form': form})

@login_required
def crear_artefacto(request, proyecto_id):
    proyecto = get_object_or_404(Project, id=proyecto_id, propietario=request.user)
    if request.method == 'POST':
        form = ArtefactoForm(request.POST)
        if form.is_valid():
            artefacto = form.save(commit=False)
            artefacto.proyecto = proyecto
            artefacto.generado_por_ia = True

            # Generar contenido con IA 👇
            artefacto.contenido = generar_artefacto_con_ia(
                tipo=artefacto.get_tipo_display(),
                nombre_proyecto=proyecto.nombre,
                descripcion=proyecto.descripcion
            )

            artefacto.save()
            return redirect('detalle_proyecto', proyecto_id=proyecto.id)
    else:
        form = ArtefactoForm()
    return render(request, 'documentacion/crear_artefacto.html', {
        'form': form,
        'proyecto': proyecto
    })

@login_required
def detalle_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Project, id=proyecto_id, propietario=request.user)
    artefactos = proyecto.artefactos.all()
    return render(request, 'documentacion/detalle_proyecto.html', {
        'proyecto': proyecto,
        'artefactos': artefactos
    })

@login_required
def ver_artefacto(request, artefacto_id):
    artefacto = get_object_or_404(Artefacto, id=artefacto_id)
    evaluaciones = artefacto.evaluaciones.all()
    return render(request, 'documentacion/ver_artefacto.html', {
        'artefacto': artefacto,
        'evaluaciones': evaluaciones
    })

def cerrar_sesion(request):
    logout(request)
    return redirect('home')  # o la página que desees

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

#def lista_proyectos(request):
   # return render(request, 'documentacion/lista_proyectos.html')  # Asegúrate de tener este template
   
@login_required
def lista_proyectos(request):
    proyectos = Project.objects.filter(propietario=request.user)
    return render(request, 'documentacion/lista_proyectos.html', {'proyectos': proyectos})

