# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 01:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nomination', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nomination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nomination_votes', to=settings.AUTH_USER_MODEL)),
                ('nominee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                              related_name='nomination_votes_received', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NominationPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='homecomingcourtnomination',
            name='female_nominee',
        ),
        migrations.RemoveField(
            model_name='homecomingcourtnomination',
            name='male_nominee',
        ),
        migrations.RemoveField(
            model_name='homecomingcourtnomination',
            name='voter',
        ),
        migrations.DeleteModel(
            name='HomecomingCourtNomination',
        ),
        migrations.AddField(
            model_name='nomination',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nominations', to='nomination.NominationPosition'),
        ),
    ]
