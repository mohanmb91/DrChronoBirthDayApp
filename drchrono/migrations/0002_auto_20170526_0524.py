# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=20)),
                ('access_token', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='chart_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='patient',
            name='date_of_birth',
            field=models.CharField(default=b'2017-05-26 05:24:40.399455', max_length=10),
        ),
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.PositiveIntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='patient',
            name='first_name',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(default=b'Male', max_length=60),
        ),
        migrations.AddField(
            model_name='patient',
            name='last_name',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.IntegerField(max_length=12, serialize=False, primary_key=True),
        ),
    ]
