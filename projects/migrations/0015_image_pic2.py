# Generated by Django 3.1.5 on 2021-02-15 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20210215_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='pic2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
