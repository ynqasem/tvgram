# Generated by Django 2.0.3 on 2018-03-20 15:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180320_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_img',
            new_name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
    ]
