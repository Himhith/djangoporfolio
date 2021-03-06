# Generated by Django 3.1.5 on 2021-02-09 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210130_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FilePathField(path='projects\\static\\img\\')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='projects\\static\\img\\'),
        ),
        migrations.AddField(
            model_name='project',
            name='images',
            field=models.ManyToManyField(related_name='projects', to='projects.Image'),
        ),
    ]
