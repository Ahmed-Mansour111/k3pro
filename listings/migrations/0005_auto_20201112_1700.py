# Generated by Django 3.1.3 on 2020-11-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20201112_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='USB_Type',
            field=models.CharField(choices=[('V8', 'V8'), ('IP', 'IPHONE'), ('TYPE-C', 'TYPE-C'), ('3.5', '3.5')], default='V8', max_length=100),
        ),
    ]
