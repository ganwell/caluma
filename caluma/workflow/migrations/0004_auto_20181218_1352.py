# SPDX-FileCopyrightText: 2019 Adfinis SyGroup AG
#
# SPDX-License-Identifier: AGPL-3.0-or-later

# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-18 13:52
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("form", "0001_initial"), ("workflow", "0003_auto_20181217_1051")]

    operations = [
        migrations.AddField(
            model_name="task",
            name="form",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="tasks",
                to="form.Form",
            ),
        ),
        migrations.AddField(
            model_name="workitem",
            name="document",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="work_item",
                to="form.Document",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="type",
            field=models.CharField(
                choices=[
                    ("simple", "Task which can only be marked as completed."),
                    (
                        "complete_workflow_form",
                        "Task completing defined workflow form.",
                    ),
                    ("complete_task_form", "Task completing defined task form."),
                ],
                max_length=50,
            ),
        ),
    ]
