# Generated by Django 4.0.4 on 2022-05-03 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmdm', '0010_alter_akc_addon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akc',
            name='addon',
            field=models.CharField(choices=[('DM22005', '报警'), ('DM22009', '分别控制')], default='', max_length=10),
        ),
    ]
