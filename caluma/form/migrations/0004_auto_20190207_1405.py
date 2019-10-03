# SPDX-FileCopyrightText: 2019 Adfinis SyGroup AG
#
# SPDX-License-Identifier: AGPL-3.0-or-later

# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-07 14:05
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("form", "0003_auto_20190130_0920")]

    operations = [
        migrations.AddField(
            model_name="form",
            name="source",
            field=models.ForeignKey(
                blank=True,
                help_text="Reference this form has been copied from",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="form.Form",
            ),
        ),
        migrations.AddField(
            model_name="option",
            name="source",
            field=models.ForeignKey(
                blank=True,
                help_text="Reference this option has been copied from",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="form.Option",
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="source",
            field=models.ForeignKey(
                blank=True,
                help_text="Reference this question has been copied from",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="form.Question",
            ),
        ),
    ]
