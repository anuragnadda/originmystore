# Generated by Django 3.1.1 on 2020-09-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0004_payment_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='expiration',
            field=models.CharField(max_length=8),
        ),
    ]
