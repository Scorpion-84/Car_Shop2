# Generated by Django 5.2 on 2025-07-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SelectCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_choice', models.CharField(max_length=300, verbose_name='انتخاب خودرو')),
                ('color_choice', models.CharField(max_length=300, verbose_name='رنگ خودرو')),
            ],
            options={
                'db_table': 'carchoice',
            },
        ),
    ]
