# Generated by Django 3.1.5 on 2021-02-10 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20210210_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FilePathField(path='\\img\\'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='\\img\\'),
        ),
    ]
