# Generated by Django 5.0.3 on 2024-03-20 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smApp', '0012_remove_plasticcollection_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plasticcollection',
            name='payment_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid')], default='pending', max_length=20),
        ),
    ]
