# Generated by Django 4.0.4 on 2022-05-03 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmdm', '0011_alter_akc_addon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akc',
            name='addon',
            field=models.CharField(choices=[('DM22005', 'DM22005'), ('DM22009', 'DM22009')], max_length=10),
        ),
    ]
