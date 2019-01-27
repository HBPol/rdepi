from django.shortcuts import render, redirect
from django.conf import settings
from coreapp.models import User, Project, Location, StudyPlan, Report, RelatedFile, LabBook
from coreapp.forms import ProjectForm, LocationForm, StudyPlanForm, ReportForm, RelatedFileForm, LabBookForm

def home(request):
    context = {'page_title': 'R&D EPI | Home'}
    return render(request, 'coreapp/home.html', context)

# Project views
def project_list(request):
    projects = Project.objects.all()
    context = {'projects': projects, 'page_title': 'R&D EPI | Projects'}
    return render(request, 'coreapp/project_list.html', context)

def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project-list')
    else:
        form = ProjectForm()
    context = {'form_project': form, 'page_title': 'R&D EPI | Create new project'}
    return render (request, 'coreapp/project_create.html', context)

def project_edit(request, id):
    pass
def project_update(request, id):
    pass
def project_delete(request, id):
    pass

# Location views
def location_list(request):
    locations = Location.objects.all()
    context = {'locations': locations, 'page_title': 'R&D EPI | Locations'}
    return render(request, 'coreapp/location_list.html', context)
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

def location_edit(request, id):
    pass
def location_update(request, id):
    pass
def location_delete(request, id):
    pass

# StudyPlan views
def studyplan_list(request):
    studyplans = StudyPlan.objects.all()
    context = {'studyplans': studyplans, 'page_title': 'R&D EPI | Study plans'}
    return render(request, 'coreapp/studyplan_list.html', context)
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
def studyplan_edit(request, id):
    pass
def studyplan_update(request, id):
    pass
def studyplan_delete(request, id):
    pass

# Report views
def report_list(request):
    reports = Report.objects.all()
    context = {'reports': reports, 'page_title': 'R&D EPI | Reports'}
    return render(request, 'coreapp/report_list.html', context)
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
def report_edit(request, id):
    pass
def report_update(request, id):
    pass
def report_delete(request, id):
    pass

# RelatedFile views
def relatedfile_list(request):
    relatedfiles = RelatedFile.objects.all()
    context = {'relatedfiles': relatedfiles, 'page_title': 'R&D EPI | Project-related files'}
    return render(request, 'coreapp/relatedfile_list.html', context)
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
def relatedfile_edit(request, id):
    pass
def relatedfile_update(request, id):
    pass
def relatedfile_delete(request, id):
    pass

# LabBook views
def labbook_list(request):
    labbooks = LabBook.objects.all()
    context = {'labbooks': labbooks, 'page_title': 'R&D EPI | Lab books'}
    return render(request, 'coreapp/labbook_list.html', context)
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
def labbook_edit(request, id):
    pass
def labbook_update(request, id):
    pass
def labbook_delete(request, id):
    pass


