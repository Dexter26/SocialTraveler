# Generated by Django 2.0.2 on 2018-03-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_active',
            field=models.IntegerField(default=1),
        ),
    ]