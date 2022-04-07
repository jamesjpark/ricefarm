# Generated by Django 4.0.2 on 2022-04-07 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField()),
                ('col', models.IntegerField()),
                ('lat', models.DecimalField(decimal_places=15, max_digits=30)),
                ('lng', models.DecimalField(decimal_places=15, max_digits=30)),
            ],
        ),
    ]
