# Generated by Django 4.0.5 on 2022-06-16 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_account_info_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_info',
            name='season',
            field=models.IntegerField(blank=True, default=7, null=True),
        ),
    ]
