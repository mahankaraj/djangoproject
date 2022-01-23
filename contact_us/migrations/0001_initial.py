# Generated by Django 3.2.9 on 2021-12-03 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام فرستنده')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=10, verbose_name='شماره تلفن')),
                ('message', models.TextField(verbose_name='پیام')),
            ],
        ),
    ]