# Generated by Django 3.2.5 on 2021-09-02 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0005_remove_comment_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='url',
            field=models.URLField(blank=True, max_length=225, null=True),
        ),
    ]
