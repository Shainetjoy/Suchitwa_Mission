# Generated by Django 5.0.3 on 2024-03-20 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smApp', '0015_delete_paymenthistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]