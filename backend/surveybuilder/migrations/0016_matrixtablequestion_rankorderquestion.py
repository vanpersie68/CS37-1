# Generated by Django 3.2.7 on 2022-09-19 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0015_matrixtable_rankorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='RankOrderQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.IntegerField(default=0)),
                ('isDropDown', models.BooleanField(default=False)),
                ('isCheckbox', models.BooleanField(default=False)),
                ('textboxMax', models.IntegerField(default=1)),
                ('textboxMin', models.IntegerField(default=1)),
                ('multipleAnswers', models.BooleanField(default=False)),
                ('otherInput', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveybuilder.question')),
            ],
        ),
        migrations.CreateModel(
            name='MatrixTableQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.IntegerField(default=0)),
                ('isDropDown', models.BooleanField(default=False)),
                ('isCheckbox', models.BooleanField(default=False)),
                ('textboxMax', models.IntegerField(default=1)),
                ('textboxMin', models.IntegerField(default=1)),
                ('multipleAnswers', models.BooleanField(default=False)),
                ('otherInput', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveybuilder.question')),
            ],
        ),
    ]