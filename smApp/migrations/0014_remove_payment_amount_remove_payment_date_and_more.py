# Generated by Django 5.0.3 on 2024-03-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smApp', '0013_plasticcollection_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.AddField(
            model_name='payment',
            name='cardDate',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='cardNumber',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='cvc',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='nameOnCard',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='streetAddress',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='user_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='zipCode',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
