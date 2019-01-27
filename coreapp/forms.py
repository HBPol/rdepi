from django.forms import ModelForm
from coreapp.models import Project, Location, StudyPlan, Report, RelatedFile, LabBook

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'prefix', 'leader']
        
class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'room_num']

class StudyPlanForm(ModelForm):
    class Meta:
        model = StudyPlan
        fields = ['author', 'project', 'location', 'efile', 'title', 'status', 'sign_date']

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['author', 'project', 'location', 'efile', 'study_plan', 'title', 'status', 'sign_date']
        
class RelatedFileForm(ModelForm):
    class Meta:
        model = RelatedFile
        fields = ['author', 'project', 'location', 'efile', 'content_descr', 'date_started', 'date_finished', 'date_archived', 'alias', 'vol_num']

class LabBookForm(ModelForm):
    class Meta:
        model = LabBook
        fields = ['author', 'project', 'location', 'efile', 'content_descr', 'date_started', 'date_finished', 'date_issued', 'index_added', 'index_num_pages']








