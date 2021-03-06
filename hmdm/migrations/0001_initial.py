# Generated by Django 4.0.4 on 2022-05-03 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AKC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.IntegerField(help_text='该AKC的订单号')),
                ('serial_number', models.CharField(help_text='该AKC的序列号', max_length=15)),
                ('salesman', models.CharField(help_text='销售人员姓名', max_length=3)),
                ('client', models.CharField(help_text='客户名称', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Addon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='该宏文件之功能代码', max_length=10)),
                ('akc', models.ManyToManyField(help_text='该宏文件之对应AKC', to='hmdm.akc')),
            ],
        ),
    ]
