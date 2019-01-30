# Generated by Django 2.1.4 on 2019-01-30 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0007_auto_20190130_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='study_plan',
        ),
        migrations.AddField(
            model_name='report',
            name='study_plan',
            field=models.ManyToManyField(to='coreapp.StudyPlan', verbose_name='Study plan(s)'),
        ),
    ]
