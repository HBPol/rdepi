# Generated by Django 2.1.2 on 2018-12-24 11:20

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('date_left', models.DateField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='LabBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_code', models.CharField(choices=[('SP', 'Study plan'), ('R', 'Report'), ('RDF', 'Related file'), ('LBN', 'Lab book'), ('OTH', 'Other')], default='OTH', max_length=3, verbose_name='Document code (e.g. study plan, report... )')),
                ('efile', models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Scanned copy')),
                ('content_descr', models.TextField(blank=True, null=True, verbose_name='Content description')),
                ('date_started', models.DateField(blank=True, null=True, verbose_name='Date started')),
                ('date_finished', models.DateField(blank=True, null=True, verbose_name='Date finished')),
                ('date_issued', models.DateField(verbose_name='Issue date')),
                ('index_added', models.BooleanField(default=False, verbose_name='Index added to project file')),
                ('index_num_pages', models.IntegerField(blank=True, null=True, verbose_name='Index number of pages')),
                ('author', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Document author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=16, null=True, verbose_name='Room')),
                ('room_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='Room number')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Project name')),
                ('prefix', models.CharField(max_length=8, verbose_name='Project code')),
                ('leader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Project leader')),
            ],
        ),
        migrations.CreateModel(
            name='RelatedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_code', models.CharField(choices=[('SP', 'Study plan'), ('R', 'Report'), ('RDF', 'Related file'), ('LBN', 'Lab book'), ('OTH', 'Other')], default='OTH', max_length=3, verbose_name='Document code (e.g. study plan, report... )')),
                ('efile', models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Scanned copy')),
                ('content_descr', models.TextField(blank=True, null=True, verbose_name='Content description')),
                ('date_started', models.DateField(blank=True, null=True, verbose_name='Date started')),
                ('date_finished', models.DateField(blank=True, null=True, verbose_name='Date finished')),
                ('date_archived', models.DateField(blank=True, null=True, verbose_name='Date archived')),
                ('alias', models.CharField(blank=True, max_length=512, null=True, verbose_name='Alias (other names this file may be known as)')),
                ('vol_num', models.IntegerField(blank=True, null=True, verbose_name='Volume number')),
                ('author', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Document author')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coreapp.Location', verbose_name='Hard copy location')),
                ('project', models.ManyToManyField(to='coreapp.Project', verbose_name='Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_code', models.CharField(choices=[('SP', 'Study plan'), ('R', 'Report'), ('RDF', 'Related file'), ('LBN', 'Lab book'), ('OTH', 'Other')], default='OTH', max_length=3, verbose_name='Document code (e.g. study plan, report... )')),
                ('efile', models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Scanned copy')),
                ('title', models.TextField(verbose_name='Report title')),
                ('status', models.CharField(choices=[('PEN', 'Pending'), ('IND', 'In draft'), ('COM', 'Complete')], default='PEN', max_length=3, verbose_name='Document status')),
                ('sign_date', models.DateField(blank=True, null=True, verbose_name='Sign-off date')),
                ('author', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Document author')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coreapp.Location', verbose_name='Hard copy location')),
                ('project', models.ManyToManyField(to='coreapp.Project', verbose_name='Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudyPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_code', models.CharField(choices=[('SP', 'Study plan'), ('R', 'Report'), ('RDF', 'Related file'), ('LBN', 'Lab book'), ('OTH', 'Other')], default='OTH', max_length=3, verbose_name='Document code (e.g. study plan, report... )')),
                ('efile', models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Scanned copy')),
                ('title', models.TextField(verbose_name='Study plan title')),
                ('status', models.CharField(choices=[('PEN', 'Pending'), ('IND', 'In draft'), ('COM', 'Complete')], default='PEN', max_length=3, verbose_name='Document status')),
                ('sign_date', models.DateField(blank=True, null=True, verbose_name='Sign-off date')),
                ('author', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Document author')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coreapp.Location', verbose_name='Hard copy location')),
                ('project', models.ManyToManyField(to='coreapp.Project', verbose_name='Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='report',
            name='study_plan',
            field=models.ManyToManyField(to='coreapp.StudyPlan', verbose_name='Study plan'),
        ),
        migrations.AddField(
            model_name='labbook',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coreapp.Location', verbose_name='Hard copy location'),
        ),
        migrations.AddField(
            model_name='labbook',
            name='project',
            field=models.ManyToManyField(to='coreapp.Project', verbose_name='Project'),
        ),
    ]
