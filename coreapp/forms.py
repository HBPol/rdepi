from django.forms import ModelForm
from coreapp.models import Project, Location, StudyPlan, Report, RelatedFile, LabBook

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        
class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

class StudyPlanForm(ModelForm):
    class Meta:
        model = StudyPlan
        fields = '__all__'

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        
class RelatedFileForm(ModelForm):
    class Meta:
        model = RelatedFile
        fields = '__all__'

class LabBookForm(ModelForm):
    class Meta:
        model = LabBook
        fields = '__all__'
        #exclude = ['date_finished']








