# Generated by Django 3.2.9 on 2021-12-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SliderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='تیتر برجسته')),
                ('subtitle', models.CharField(max_length=128, verbose_name='توضیحات')),
                ('picture', models.ImageField(upload_to='sliders/pics/', verbose_name='عکس اسلایدر')),
                ('buy_link', models.URLField(verbose_name='لینک خرید')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر ها',
            },
        ),
    ]