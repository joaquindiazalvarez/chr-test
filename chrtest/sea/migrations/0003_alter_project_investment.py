# Generated by Django 4.1.7 on 2023-02-16 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sea', '0002_rename_inversion_project_investment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='investment',
            field=models.FloatField(),
        ),
    ]
