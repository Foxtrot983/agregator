# Generated by Django 3.1.7 on 2021-03-02 23:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('value_buy', models.FloatField(null=True)),
                ('value_sell', models.FloatField(null=True)),
                ('value_nb', models.FloatField(null=True)),
                ('time', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Данные по валюте',
                'verbose_name_plural': 'Данные по валютам',
            },
        ),
    ]
