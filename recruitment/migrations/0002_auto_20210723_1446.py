# Generated by Django 3.1.2 on 2021-07-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
