# Generated by Django 5.0.3 on 2024-04-23 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smApp', '0021_alter_customer_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='plasticcollectionschedule',
            name='staff',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
