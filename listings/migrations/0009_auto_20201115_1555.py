# Generated by Django 3.1.3 on 2020-11-15 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20201115_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='image_height',
            new_name='photo_main_height',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='image_width',
            new_name='photo_main_width',
        ),
    ]
