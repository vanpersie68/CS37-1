# Generated by Django 3.2.7 on 2022-09-15 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0013_survey_camera'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialpostquestion',
            name='articleUser',
            field=models.CharField(blank=True, default='', max_length=5000),
        ),
    ]