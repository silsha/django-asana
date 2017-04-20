# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djasana', '0007_auto_20170418_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(to='djasana.Tag'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_at',
            field=models.DateTimeField(null=True),
        ),
    ]