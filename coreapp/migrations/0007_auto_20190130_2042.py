# Generated by Django 2.1.4 on 2019-01-30 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0006_auto_20190130_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labbook',
            name='project',
        ),
        migrations.AddField(
            model_name='labbook',
            name='project',
            field=models.ManyToManyField(to='coreapp.Project', verbose_name='Associated project(s)'),
        ),
        migrations.RemoveField(
            model_name='relatedfile',
            name='project',
        ),
        migrations.AddField(
            model_name='relatedfile',
            name='project',
            field=models.ManyToManyField(to='coreapp.Project', verbose_name='Associated project(s)'),
        ),
        migrations.RemoveField(
            model_name='report',
            name='project',
        ),
        migrations.AddField(
            model_name='report',
            name='project',
            field=models.ManyToManyField(to='coreapp.Project', verbose_name='Associated project(s)'),
        ),
        migrations.RemoveField(
            model_name='studyplan',
            name='project',
        ),
        migrations.AddField(
            model_name='studyplan',
            name='project',
            field=models.ManyToManyField(to='coreapp.Project', verbose_name='Associated project(s)'),
        ),
    ]
