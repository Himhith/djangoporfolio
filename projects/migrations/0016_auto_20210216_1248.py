# Generated by Django 3.1.5 on 2021-02-16 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_image_pic2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.RemoveField(
            model_name='image',
            name='pic2',
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/images'),
        ),
    ]
