# Generated by Django 5.0.3 on 2024-03-19 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smApp', '0005_educationalresource_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='plasticcollection',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
