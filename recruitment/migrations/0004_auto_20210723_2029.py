# Generated by Django 3.1.2 on 2021-07-23 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0003_auto_20210723_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediateamrecs',
            name='other_interests',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='mediateamrecs',
            name='other_skills',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='webteamrecs',
            name='other_skills',
            field=models.CharField(default='-', max_length=200),
        ),
    ]
