# Generated by Django 3.1.3 on 2020-11-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_listing_list_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=80)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/home-image/')),
            ],
        ),
    ]
