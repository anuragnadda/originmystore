# Generated by Django 3.1.1 on 2020-09-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
