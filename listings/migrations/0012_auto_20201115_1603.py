# Generated by Django 3.1.3 on 2020-11-15 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_auto_20201115_1600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='photo',
            new_name='photo_main',
        ),
    ]
