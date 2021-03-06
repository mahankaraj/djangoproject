# Generated by Django 2.2.24 on 2022-01-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandmodel',
            name='ram',
            field=models.CharField(default='', max_length=3, verbose_name='رم'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brandmodel',
            name='sim',
            field=models.CharField(default='', max_length=1, verbose_name='تعداد سیم کارت'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brandmodel',
            name='time_make',
            field=models.CharField(default='', max_length=1, verbose_name='تعداد سیم کارت'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brandmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='brandmodel',
            name='price',
            field=models.CharField(max_length=20, verbose_name='قیمت برند'),
        ),
    ]
