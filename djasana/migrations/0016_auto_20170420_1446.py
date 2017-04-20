# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 18:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djasana', '0015_auto_20170420_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='hearted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='story',
            name='hearts',
            field=models.ManyToManyField(related_name='story_hearted', to='djasana.User'),
        ),
        migrations.AddField(
            model_name='story',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='num_hearts',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='source',
            field=models.CharField(choices=[('web', 'web')], default='web', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='target',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='djasana.Task'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='type',
            field=models.CharField(choices=[('comment', 'comment'), ('system', 'system')], default=1, max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='hearted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='hearts',
            field=models.ManyToManyField(related_name='task_hearted', to='djasana.User'),
        ),
    ]