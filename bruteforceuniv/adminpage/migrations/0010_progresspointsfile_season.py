# Generated by Django 3.2.5 on 2021-10-14 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminpage", "0009_auto_20210924_1423"),
    ]

    operations = [
        migrations.AddField(
            model_name="progresspointsfile",
            name="season",
            field=models.IntegerField(default=7),
            preserve_default=False,
        ),
    ]
