# Generated by Django 2.0.3 on 2018-03-21 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_profile_profile_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
    ]
