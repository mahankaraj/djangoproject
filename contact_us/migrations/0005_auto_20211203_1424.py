# Generated by Django 3.2.9 on 2021-12-03 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0004_auto_20211203_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='pic1',
            field=models.ImageField(default='', upload_to='about/pics/', verbose_name='عکس اول'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutus',
            name='pic2',
            field=models.ImageField(default='', upload_to='about/pics/', verbose_name='عکس دوم'),
            preserve_default=False,
        ),
    ]