# Generated by Django 4.0.2 on 2022-04-07 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Farm',
        ),
    ]
