from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Project, Location, StudyPlan, Report, RelatedFile, LabBook

admin.site.register(User, UserAdmin)
admin.site.register(Project)
admin.site.register(Location)
admin.site.register(StudyPlan)
admin.site.register(Report)
admin.site.register(RelatedFile)
admin.site.register(LabBook)
