from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0032_auto_20230525_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='visible',
            field=models.IntegerField(default=1),
        ),
    ]
