# Generated by Django 3.2.5 on 2021-09-01 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0002_auto_20210901_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
