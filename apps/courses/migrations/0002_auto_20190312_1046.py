# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-12 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20190310_1945'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coures',
            name='coures_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.CouresOrg', verbose_name='机构名称'),
        ),
        migrations.AddField(
            model_name='coures',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Teacher', verbose_name='讲师'),
        ),
    ]
