from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.home, name='home'),
    
    # The following are specific paths to display list of documents filtering by a specific project
    path('project/<int:id>/index', views.project_index, name='project-index'),
    path('project/<int:id>/studyplan', views.project_studyplan_list, name='project-studyplan-list'),
    path('project/<int:id>/report', views.project_report_list, name='project-report-list'),
    path('project/<int:id>/relatedfile', views.project_relatedfile_list, name='project-relatedfile-list'),
    path('project/<int:id>/labbook', views.project_labbook_list, name='project-labbook-list'),
    
    # These are specific for creating new documents for a specific project
    path('studyplan/create/project/<int:id>', views.project_studyplan_create, name='project-studyplan-create'),
    path('report/create/project/<int:id>', views.project_report_create, name='project-report-create'),
    path('relatedfile/create/project/<int:id>', views.project_relatedfile_create, name='project-relatedfile-create'),
    path('labbook/create/project/<int:id>', views.project_labbook_create, name='project-labbook-create'),
    
    # And the following are the usual paths for a basic CRUD with no initial filtering
    path('project/', views.project_list, name='project-list'),
    path('project/create/', views.project_create, name='project-create'),
    path('project/edit/<int:id>', views.project_edit, name='project-edit'),
    path('project/<int:id>', views.project_detail, name='project-detail'),
    path('project/edit/update/<int:id>', views.project_update, name='project-update'),
    path('project/delete/<int:id>', views.project_delete, name='project-delete'),
    
    path('location/', views.location_list, name='location-list'),
    path('location/create/', views.location_create, name='location-create'),
    path('location/edit/<int:id>', views.location_edit, name='location-edit'),
    path('location/<int:id>', views.location_detail, name='location-detail'),
    path('location/edit/update/<int:id>', views.location_update, name='location-update'),
    path('location/delete/<int:id>', views.location_delete, name='location-delete'),
    
    path('studyplan/', views.studyplan_list, name='studyplan-list'),
    path('studyplan/create/', views.studyplan_create, name='studyplan-create'),
    path('studyplan/edit/<int:id>', views.studyplan_edit, name='studyplan-edit'),
    path('studyplan/<int:id>', views.studyplan_detail, name='studyplan-detail'),
    path('studyplan/edit/update/<int:id>', views.studyplan_update, name='studyplan-update'),
    path('studyplan/delete/<int:id>', views.studyplan_delete, name='studyplan-delete'),
    
    
    path('report/', views.report_list, name='report-list'),
    path('report/create/', views.report_create, name='report-create'),
    path('report/edit/<int:id>', views.report_edit, name='report-edit'),
    path('report/<int:id>', views.report_detail, name='report-detail'),
    path('report/edit/update/<int:id>', views.report_update, name='report-update'),
    path('report/delete/<int:id>', views.report_delete, name='report-delete'),
    
    path('relatedfile/', views.relatedfile_list, name='relatedfile-list'),
    path('relatedfile/create/', views.relatedfile_create, name='relatedfile-create'),
    path('relatedfile/edit/<int:id>', views.relatedfile_edit, name='relatedfile-edit'),
    path('relatedfile/<int:id>', views.relatedfile_detail, name='relatedfile-detail'),
    path('relatedfile/edit/update/<int:id>', views.relatedfile_update, name='relatedfile-update'),
    path('relatedfile/delete/<int:id>', views.relatedfile_delete, name='relatedfile-delete'),
    
    path('labbook/', views.labbook_list, name='labbook-list'),
    path('labbook/create/', views.labbook_create, name='labbook-create'),
    path('labbook/edit/<int:id>', views.labbook_edit, name='labbook-edit'),
    path('labbook/<int:id>', views.labbook_detail, name='labbook-detail'),
    path('labbook/edit/update/<int:id>', views.labbook_update, name='labbook-update'),
    path('labbook/delete/<int:id>', views.labbook_delete, name='labbook-delete'),
]