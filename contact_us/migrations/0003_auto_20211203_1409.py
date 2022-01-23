# Generated by Django 3.2.9 on 2021-12-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0002_auto_20211203_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information1', models.TextField(verbose_name='بخش یک اطلاعات')),
                ('information2', models.TextField(verbose_name='بخش دو اطلاعات')),
            ],
            options={
                'verbose_name': 'درباره ما',
                'verbose_name_plural': 'درباره ما',
            },
        ),
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': 'تماس با ما', 'verbose_name_plural': 'تماس های با ما'},
        ),
    ]
