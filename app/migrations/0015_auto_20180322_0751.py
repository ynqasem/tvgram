# Generated by Django 2.0.3 on 2018-03-22 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20180321_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='following',
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]