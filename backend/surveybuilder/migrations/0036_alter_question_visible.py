from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0037_question_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='visible',
            field=models.IntegerField(default=1),
        ),
    ]
