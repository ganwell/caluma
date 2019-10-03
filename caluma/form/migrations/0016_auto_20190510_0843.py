# SPDX-FileCopyrightText: 2019 Adfinis SyGroup AG
#
# SPDX-License-Identifier: AGPL-3.0-or-later

# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-10 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("form", "0015_question_format_validators")]

    operations = [
        migrations.AlterField(
            model_name="questionoption",
            name="id",
            field=models.CharField(
                max_length=255, primary_key=True, serialize=False, unique=True
            ),
        )
    ]
