# SPDX-FileCopyrightText: 2019 Adfinis SyGroup AG
#
# SPDX-License-Identifier: AGPL-3.0-or-later

# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-21 15:17
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("form", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="created_by_group",
            field=models.CharField(
                blank=True, db_index=True, max_length=150, null=True
            ),
        ),
        migrations.AlterField(
            model_name="answer",
            name="meta",
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="document",
            name="created_by_group",
            field=models.CharField(
                blank=True, db_index=True, max_length=150, null=True
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="meta",
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="form",
            name="created_by_group",
            field=models.CharField(
                blank=True, db_index=True, max_length=150, null=True
            ),
        ),
        migrations.AlterField(
            model_name="form",
            name="meta",
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="formquestion",
            name="created_by_group",
            field=models.CharField(
                blank=True, db_index=True, max_length=150, null=True
            ),
        ),
        migrations.AlterField(
            model_name="option",
            name="created_by_group",
            field=models.CharField(
                blank=True, db_index=True, max_length=150, null=True
            ),
        ),
        migrations.AlterField(
            model_name="option",
            name="meta",
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="question",
            name="configuration",
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="question",
            name="created_by_group",
            field=models.CharField(
                blank=True, db_index=True, max_length=150, null=True
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="meta",
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="questionoption",
            name="created_by_group",
            field=models.CharField(
                blank=True, db_index=True, max_length=150, null=True
            ),
        ),
    ]
