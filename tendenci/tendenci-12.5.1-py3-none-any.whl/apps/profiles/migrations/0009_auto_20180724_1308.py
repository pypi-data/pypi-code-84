# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-24 13:08


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20180315_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(blank=True, max_length=100, verbose_name='highest level of education'),
        ),
    ]
