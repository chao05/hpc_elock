# Generated by Django 4.0.4 on 2022-05-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmdm', '0003_alter_addongeneral_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akc',
            name='po_number',
            field=models.CharField(help_text='该AKC的订单号', max_length=10),
        ),
    ]
