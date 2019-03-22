# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-21 17:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("form", "0008_auto_20190319_1720")]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="value_document",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="parent_answers",
                to="form.Document",
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="sub_form",
            field=models.ForeignKey(
                blank=True,
                help_text="Form referenced in a FormQuestion",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="form.Form",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="row_form",
            field=models.ForeignKey(
                blank=True,
                help_text="Form that represents rows of a TableQuestion",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="form.Form",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="type",
            field=models.CharField(
                choices=[
                    ("multiple_choice", "multiple_choice"),
                    ("integer", "integer"),
                    ("float", "float"),
                    ("date", "date"),
                    ("choice", "choice"),
                    ("textarea", "textarea"),
                    ("text", "text"),
                    ("table", "table"),
                    ("form", "form"),
                ],
                max_length=15,
            ),
        ),
    ]
