from django import forms
from .models import Project, Artefacto

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['nombre', 'descripcion']

class ArtefactoForm(forms.ModelForm):
    class Meta:
        model = Artefacto
        fields = ['tipo', 'titulo', 'contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 6})
        }
