# Generated by Django 3.1.3 on 2020-11-11 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rep', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('photo_main', models.ImageField(upload_to='')),
                ('photo_1', models.ImageField(blank=True, upload_to='')),
                ('photo_2', models.ImageField(blank=True, upload_to='')),
                ('photo_3', models.ImageField(blank=True, upload_to='')),
                ('photo_4', models.ImageField(blank=True, upload_to='')),
                ('photo_5', models.ImageField(blank=True, upload_to='')),
                ('is_published', models.BooleanField(default=True)),
                ('rep', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rep.rep')),
            ],
        ),
    ]
