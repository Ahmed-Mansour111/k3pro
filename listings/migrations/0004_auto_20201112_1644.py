# Generated by Django 3.1.3 on 2020-11-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20201112_1400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='listing',
            name='USB_Type',
            field=models.CharField(choices=[('V8', 'V8'), ('IP', 'IPHONE'), ('TYPE-C', 'TYPE-C')], default='V8', max_length=100),
        ),
    ]