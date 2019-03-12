from django.shortcuts import render, redirect
from django.conf import settings
from coreapp.models import User, Project, Location, StudyPlan, Report, RelatedFile, LabBook
from coreapp.forms import ProjectForm, LocationForm, StudyPlanForm, ReportForm, RelatedFileForm, LabBookForm

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {'page_title': 'R&D EPI | Home'}
    return render(request, 'coreapp/home.html', context)

# Project views
@login_required
def project_list(request):
    projects = Project.objects.all()
    context = {'projects': projects, 'page_title': 'R&D EPI | Projects'}
    return render(request, 'coreapp/project_list.html', context)

@login_required
def project_detail(request, id):
    project = Project.objects.get(id=id)
    context = {'project': project, 'page_title': 'R&D EPI | Project details'}
    return render(request, 'coreapp/project_detail.html', context)
@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project-list')
    else:
        user = request.user
        form = ProjectForm(initial={'leader': user.id})
    context = {'form_project': form, 'page_title': 'R&D EPI | Create new project'}
    return render (request, 'coreapp/project_create.html', context)
@login_required
def project_edit(request, id):
    project = Project.objects.get(id=id)
    # Use instance of project to instantiate the from with initial values for the project with id=id
    form = ProjectForm(instance=project)
    context = {'project': project, 'form_project': form, 'page_title': 'R&D EPI | Edit project'}
    return render(request, 'coreapp/project_edit.html', context)
@login_required
def project_update(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('project-list')
@login_required    
def project_delete(request, id):
    pass

# Location views
@login_required
def location_list(request):
    locations = Location.objects.all()
    context = {'locations': locations, 'page_title': 'R&D EPI | Locations'}
    return render(request, 'coreapp/location_list.html', context)
@login_required
def location_detail(request, id):
    location = Location.objects.get(id=id)
    context = {'location': location, 'page_title': 'R&D EPI | Location details'}
    return render(request, 'coreapp/location_detail.html', context)
@login_required
def location_create(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location-list')
    else:
        form = LocationForm()
    context = {'form_location': form, 'page_title': 'R&D EPI | Create new Location'}
    return render (request, 'coreapp/location_create.html', context)
@login_required
def location_edit(request, id):
    location = Location.objects.get(id=id)
    form = LocationForm(instance=location)
    context = {'location': location, 'form_location': form, 'page_title': 'R&D EPI | Edit location'}
    return render(request, 'coreapp/location_edit.html', context)
@login_required
def location_update(request, id):
    location = Location.objects.get(id=id)
    form = LocationForm(request.POST or None, instance=location)
    if form.is_valid():
        form.save()
        return redirect('location-list')
@login_required
def location_delete(request, id):
    pass

# StudyPlan views
@login_required
def studyplan_list(request):
    studyplans = StudyPlan.objects.all()
    context = {'studyplans': studyplans, 'page_title': 'R&D EPI | Study plans'}
    return render(request, 'coreapp/studyplan_list.html', context)

@login_required
def studyplan_detail(request, id):
    studyplan = StudyPlan.objects.get(id=id)
    context = {'studyplan': studyplan, 'page_title': 'R&D EPI | Study Plan details'}
    return render(request, 'coreapp/studyplan_detail.html', context)
@login_required
def studyplan_create(request):
    if request.method == "POST":
        form = StudyPlanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('studyplan-list')
    else:
        form = StudyPlanForm()
    context = {'form_studyplan': form, 'page_title': 'R&D EPI | Create new study plan'}
    return render (request, 'coreapp/studyplan_create.html', context)
@login_required
def studyplan_edit(request, id):
    studyplan = StudyPlan.objects.get(id=id)
    form = StudyPlanForm(instance=studyplan)
    context = {'studyplan': studyplan, 'form_studyplan': form, 'page_title': 'R&D EPI | Edit study plan'}
    return render(request, 'coreapp/studyplan_edit.html', context)
@login_required
def studyplan_update(request, id):
    studyplan = StudyPlan.objects.get(id=id)
    form = StudyPlanForm(request.POST, request.FILES, instance=studyplan)
    if form.is_valid():
        form.save()
        return redirect('studyplan-list')
@login_required
def studyplan_delete(request, id):
    pass

# Report views
@login_required
def report_list(request):
    reports = Report.objects.all()
    context = {'reports': reports, 'page_title': 'R&D EPI | Reports'}
    return render(request, 'coreapp/report_list.html', context)
@login_required
def report_detail(request, id):
    report = Report.objects.get(id=id)
    context = {'report': report, 'page_title': 'R&D EPI | Report details'}
    return render(request, 'coreapp/report_detail.html', context)
@login_required
def report_create(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('report-list')
    else:
        form = ReportForm()
    context = {'form_report': form, 'page_title': 'R&D EPI | Create new report'}
    return render (request, 'coreapp/report_create.html', context)
@login_required
def report_edit(request, id):
    report = Report.objects.get(id=id)
    form = ReportForm(instance=report)
    context = {'report': report, 'form_report': form, 'page_title': 'R&D EPI | Edit report'}
    return render(request, 'coreapp/report_edit.html', context)
@login_required
def report_update(request, id):
    report = Report.objects.get(id=id)
    form = ReportForm(request.POST, request.FILES, instance=report)
    if form.is_valid():
        form.save()
        return redirect('report-list')
@login_required
def report_delete(request, id):
    pass

# RelatedFile views
@login_required
def relatedfile_list(request):
    relatedfiles = RelatedFile.objects.all()
    context = {'relatedfiles': relatedfiles, 'page_title': 'R&D EPI | Project-related files'}
    return render(request, 'coreapp/relatedfile_list.html', context)
@login_required
def relatedfile_detail(request, id):
    relatedfile = RelatedFile.objects.get(id=id)
    context = {'relatedfile': relatedfile, 'page_title': 'R&D EPI | Related file details'}
    return render(request, 'coreapp/relatedfile_detail.html', context)
@login_required
def relatedfile_create(request):
    if request.method == "POST":
        form = RelatedFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('relatedfile-list')
    else:
        form = RelatedFileForm()
    context = {'form_relatedfile': form, 'page_title': 'R&D EPI | Create new related file'}
    return render (request, 'coreapp/relatedfile_create.html', context)
@login_required
def relatedfile_edit(request, id):
    relatedfile = RelatedFile.objects.get(id=id)
    form = RelatedFileForm(instance=relatedfile)
    context = {'relatedfile': relatedfile, 'form_relatedfile': form, 'page_title': 'R&D EPI | Edit related file'}
    return render(request, 'coreapp/relatedfile_edit.html', context)
@login_required
def relatedfile_update(request, id):
    relatedfile = RelatedFile.objects.get(id=id)
    form = RelatedFileForm(request.POST, request.FILES, instance=relatedfile)
    if form.is_valid():
        form.save()
        return redirect('relatedfile-list')
@login_required
def relatedfile_delete(request, id):
    pass

# LabBook views
@login_required
def labbook_list(request):
    labbooks = LabBook.objects.all()
    context = {'labbooks': labbooks, 'page_title': 'R&D EPI | Lab books'}
    return render(request, 'coreapp/labbook_list.html', context)
@login_required
def labbook_detail(request, id):
    labbook = LabBook.objects.get(id=id)
    context = {'labbook': labbook, 'page_title': 'R&D EPI | Lab book details'}
    return render(request, 'coreapp/labbook_detail.html', context)
@login_required
def labbook_create(request):
    if request.method == "POST":
        form = LabBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('labbook-list')
    else:
        form = LabBookForm()
    context = {'form_labbook': form, 'page_title': 'R&D EPI | Create new lab book'}
    return render (request, 'coreapp/labbook_create.html', context)
@login_required
def labbook_edit(request, id):
    labbook = LabBook.objects.get(id=id)
    form = LabBookForm(instance=labbook)
    context = {'labbook': labbook, 'form_labbook': form, 'page_title': 'R&D EPI | Edit related file'}
    return render(request, 'coreapp/labbook_edit.html', context)
@login_required
def labbook_update(request, id):
    labbook = LabBook.objects.get(id=id)
    form = LabBookForm(request.POST, request.FILES, instance=labbook)
    if form.is_valid():
        form.save()
        return redirect('labbook-list')
@login_required
def labbook_delete(request, id):
    pass

# List views filtered by project
@login_required
def project_index(request, id):
    project = Project.objects.get(id=id)
    context = {'project': project, 'page_title': 'R&D EPI | Project index'}
    return render(request, 'coreapp/project_index.html', context)
@login_required
def project_studyplan_list(request, id):
    studyplans = StudyPlan.objects.filter(project_id=id)
    project = Project.objects.get(id=id)
    context = {'studyplans': studyplans, 'project': project, 'page_title': 'R&D EPI | Study plans'}
    return render(request, 'coreapp/project_studyplan_list.html', context)
@login_required
def project_report_list(request, id):
    reports = Report.objects.filter(project_id=id)
    project = Project.objects.get(id=id)
    context = {'reports': reports, 'project': project, 'page_title': 'R&D EPI | Reports'}
    return render(request, 'coreapp/project_report_list.html', context)
@login_required
def project_relatedfile_list(request, id):
    relatedfiles = RelatedFile.objects.filter(project=id)
    project = Project.objects.get(id=id)
    context = {'relatedfiles': relatedfiles, 'project': project, 'page_title': 'R&D EPI | Related files'}
    return render(request, 'coreapp/project_relatedfile_list.html', context)
@login_required
def project_labbook_list(request, id):
    labbooks = LabBook.objects.filter(project=id)
    project = Project.objects.get(id=id)
    context = {'labbooks': labbooks, 'project': project, 'page_title': 'R&D EPI | Lab books'}
    return render(request, 'coreapp/project_labbook_list.html', context)

# New views to add new documents with pre-selected values for project and user (logged user).
# TODO: consider implementing this in the "studyplan_create" function... no need to have two functions to do almost the same thing.
@login_required
def project_studyplan_create(request, id):
    if request.method == "POST":
        form = StudyPlanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project-studyplan-list', id=id)
    else:
        project = Project.objects.get(id=id)
        user = request.user
        form = StudyPlanForm(initial={'project': project.id, 'author': user.id})
    context = {'form_studyplan': form, 'page_title': 'R&D EPI | Create new study plan'}
    return render (request, 'coreapp/studyplan_create.html', context)




