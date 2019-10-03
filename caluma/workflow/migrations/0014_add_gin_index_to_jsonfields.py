# SPDX-FileCopyrightText: 2019 Adfinis SyGroup AG
#
# SPDX-License-Identifier: AGPL-3.0-or-later

# Generated by Django 2.2.3 on 2019-07-29 09:08

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("workflow", "0013_auto_20190718_1235")]

    operations = [
        migrations.AddIndex(
            model_name="case",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["meta"], name="workflow_ca_meta_08775a_gin"
            ),
        ),
        migrations.AddIndex(
            model_name="task",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["meta"], name="workflow_ta_meta_6864a4_gin"
            ),
        ),
        migrations.AddIndex(
            model_name="workflow",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["meta"], name="workflow_wo_meta_2ac517_gin"
            ),
        ),
        migrations.AddIndex(
            model_name="workitem",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["meta"], name="workflow_wo_meta_2704a2_gin"
            ),
        ),
    ]
