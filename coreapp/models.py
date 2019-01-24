from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

DOCUMENT_CODE = (
        ('SP', 'Study plan'),
        ('R', 'Report'),
        ('RDF', 'Related file'),
        ('LBN', 'Lab book'),
        ('OTH', 'Other'),
    )

DOCUMENT_STATUS = (
        ('PEN', 'Pending'),
        ('IND', 'In draft'),
        ('COM', 'Complete'),
    )

class User (AbstractUser):
    # Extending AbstractUser to create a custom user model
    date_left = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.get_full_name()

class Project(models.Model):
    name = models.CharField("Project name", max_length=128)
    leader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Project leader")
    prefix = models.CharField("Project code", max_length=8)
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField("Room", max_length=16, null=True, blank=True)
    room_num = models.CharField("Room number", max_length=16, null=True, blank=True)
    def __str__(self):
        return self.name

class Document(models.Model):
    # It is assumed each document has one author only (many-to-one)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Main author")
    # Similarly, for the prototype only, it is assumed each document belongs to one project only (many-to-one)
    # TODO: 'project' is set here as many-to-one here, but consider many-to-many in the final version, because some documents may be associated with more than one project (e.g. raw data files or labbooks ...)
    # project = models.ManyToManyField(Project, verbose_name="Associated project(s)")
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Associated project")
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Hard copy location")
    document_code = models.CharField("Document code (e.g. study plan, report... )", max_length=3, choices=DOCUMENT_CODE, default='OTH')
    efile = models.FileField("Scanned copy", upload_to='uploads/', null=True, blank=True)
    class Meta:
        abstract = True

class StudyPlan(Document):
    title = models.TextField("Study plan title")
    status = models.CharField("Document status", max_length=3, choices=DOCUMENT_STATUS, default='PEN')
    document_code = 'SP'
    sign_date = models.DateField("Sign-off date", null=True, blank=True)
    def __str__(self):
        return self.title

class Report(Document):
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Study plan") # It is assumed each report has one study plan only (many-to-one)
    title = models.TextField("Report title")
    status = models.CharField("Document status", max_length=3, choices=DOCUMENT_STATUS, default='PEN')
    document_code = 'R'
    sign_date = models.DateField("Sign-off date", null=True, blank=True)
    def __str__(self):
        return self.title
    
class RelatedFile(Document):
    content_descr = models.TextField("Content description", null=True, blank=True)
    date_started = models.DateField("Date started", null=True, blank=True)
    date_finished = models.DateField("Date finished", null=True, blank=True)
    date_archived = models.DateField("Date archived", null=True, blank=True)
    alias = models.CharField("Alias (other names this file may be known as)", max_length=512, null=True, blank=True)
    vol_num = models.IntegerField("Volume number", null=True, blank=True)
    document_code = 'RDF'
    def __str__(self):
        return self.content_descr

class LabBook(Document):
    content_descr = models.TextField("Content description", null=True, blank=True)
    date_started = models.DateField("Date started", null=True, blank=True)
    date_finished = models.DateField("Date finished", null=True, blank=True)
    date_issued = models.DateField("Issue date")
    index_added = models.BooleanField("Index added to project file", default=False)
    index_num_pages = models.IntegerField("Index number of pages", null=True, blank=True)
    document_code = 'LBN'
    def __str__(self):
        return self.content_descr

