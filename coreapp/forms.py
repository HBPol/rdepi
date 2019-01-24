from django.forms import ModelForm
from coreapp.models import Project

class ProjectForm(ModelForm):
    class Meta:
        Project
        fields = ['name', 'leader', 'prefix']