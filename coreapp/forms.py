from django.forms import ModelForm
from coreapp.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'prefix', 'leader']