from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('project/', views.project_index, name='project-index'),
    path('project/create/', views.project_create, name='project-create'),
    path('project/edit/<int:id>', views.project_edit, name='project-edit'),
    path('project/edit/update/<int:id>', views.project_update, name='project-update'),
    path('project/delete/<int:id>', views.project_delete, name='project-delete'),
    
    path('location/', views.location_index, name='location-index'),
    path('location/create/', views.location_create, name='location-create'),
    path('location/edit/<int:id>', views.location_edit, name='location-edit'),
    path('location/edit/update/<int:id>', views.location_update, name='location-update'),
    path('location/delete/<int:id>', views.location_delete, name='location-delete'),
    
    path('studyplan/', views.studyplan_index, name='studyplan-index'),
    path('studyplan/create/', views.studyplan_create, name='studyplan-create'),
    path('studyplan/edit/<int:id>', views.studyplan_edit, name='studyplan-edit'),
    path('studyplan/edit/update/<int:id>', views.studyplan_update, name='studyplan-update'),
    path('studyplan/delete/<int:id>', views.studyplan_delete, name='studyplan-delete'),
    
    path('report/', views.report_index, name='report-index'),
    path('report/create/', views.report_create, name='report-create'),
    path('report/edit/<int:id>', views.report_edit, name='report-edit'),
    path('report/edit/update/<int:id>', views.report_update, name='report-update'),
    path('report/delete/<int:id>', views.report_delete, name='report-delete'),
    
    path('relatedfile/', views.relatedfile_index, name='relatedfile-index'),
    path('relatedfile/create/', views.relatedfile_create, name='relatedfile-create'),
    path('relatedfile/edit/<int:id>', views.relatedfile_edit, name='relatedfile-edit'),
    path('relatedfile/edit/update/<int:id>', views.relatedfile_update, name='relatedfile-update'),
    path('relatedfile/delete/<int:id>', views.relatedfile_delete, name='relatedfile-delete'),
    
    path('labbook/', views.labbook_index, name='labbook-index'),
    path('labbook/create/', views.labbook_create, name='labbook-create'),
    path('labbook/edit/<int:id>', views.labbook_edit, name='labbook-edit'),
    path('labbook/edit/update/<int:id>', views.labbook_update, name='labbook-update'),
    path('labbook/delete/<int:id>', views.labbook_delete, name='labbook-delete'),
]