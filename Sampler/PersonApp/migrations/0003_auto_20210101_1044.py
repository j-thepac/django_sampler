# Generated by Django 3.1.4 on 2021-01-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonApp', '0002_person_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
